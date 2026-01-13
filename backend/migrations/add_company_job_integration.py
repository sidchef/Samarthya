"""
Add company_job_id and related fields to opportunities table
This enables full integration between company_job_postings and opportunities
"""

import mysql.connector
from mysql.connector import Error

# TiDB Cloud connection details
config = {
    'host': 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '2p6u58mMBxe8vS4.root',
    'password': 'Z9A4YzsaLtwXXHmZ',
    'database': 'samarthya_db',
    'ssl_ca': 'isrgrootx1.pem',
    'ssl_verify_cert': True,
    'ssl_verify_identity': True
}

def add_company_job_integration():
    """Add company_job_id and related fields to opportunities table"""
    connection = None
    try:
        print("🔄 Connecting to TiDB Cloud database...")
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        print("✅ Connected successfully!")
        
        # Check if company_job_id column already exists
        print("\n🔍 Checking if company_job_id column already exists...")
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND COLUMN_NAME = 'company_job_id'
        """)
        
        if cursor.fetchone():
            print("⚠️  company_job_id column already exists.")
        else:
            print("➕ Adding company_job_id column to opportunities table...")
            cursor.execute("""
                ALTER TABLE opportunities 
                ADD COLUMN company_job_id INT AFTER org_sector_id
            """)
            connection.commit()
            print("✅ company_job_id column added!")
        
        # Check and add skills column
        print("\n🔍 Checking if skills column exists in opportunities...")
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND COLUMN_NAME = 'skills'
        """)
        
        if cursor.fetchone():
            print("⚠️  skills column already exists.")
        else:
            print("➕ Adding skills column to opportunities table...")
            cursor.execute("""
                ALTER TABLE opportunities 
                ADD COLUMN skills TEXT AFTER duration
            """)
            connection.commit()
            print("✅ skills column added!")
        
        # Check and add description column
        print("\n🔍 Checking if description column exists in opportunities...")
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND COLUMN_NAME = 'description'
        """)
        
        if cursor.fetchone():
            print("⚠️  description column already exists.")
        else:
            print("➕ Adding description column to opportunities table...")
            cursor.execute("""
                ALTER TABLE opportunities 
                ADD COLUMN description TEXT AFTER skills
            """)
            connection.commit()
            print("✅ description column added!")
        
        # Check and add vacancies column
        print("\n🔍 Checking if vacancies column exists in opportunities...")
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND COLUMN_NAME = 'vacancies'
        """)
        
        if cursor.fetchone():
            print("⚠️  vacancies column already exists.")
        else:
            print("➕ Adding vacancies column to opportunities table...")
            cursor.execute("""
                ALTER TABLE opportunities 
                ADD COLUMN vacancies INT DEFAULT 1 AFTER description
            """)
            connection.commit()
            print("✅ vacancies column added!")
        
        # Check and add min_score column
        print("\n🔍 Checking if min_score column exists in opportunities...")
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND COLUMN_NAME = 'min_score'
        """)
        
        if cursor.fetchone():
            print("⚠️  min_score column already exists.")
        else:
            print("➕ Adding min_score column to opportunities table...")
            cursor.execute("""
                ALTER TABLE opportunities 
                ADD COLUMN min_score DECIMAL(5,2) DEFAULT 0 AFTER vacancies
            """)
            connection.commit()
            print("✅ min_score column added!")
        
        # Add foreign key constraint if doesn't exist
        print("\n🔗 Checking foreign key constraint...")
        cursor.execute("""
            SELECT CONSTRAINT_NAME 
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
            WHERE TABLE_SCHEMA = 'samarthya_db' 
            AND TABLE_NAME = 'opportunities' 
            AND CONSTRAINT_NAME = 'fk_opportunities_company_job'
        """)
        
        if cursor.fetchone():
            print("ℹ️  Foreign key constraint already exists")
        else:
            try:
                print("➕ Adding foreign key constraint...")
                cursor.execute("""
                    ALTER TABLE opportunities
                    ADD CONSTRAINT fk_opportunities_company_job
                    FOREIGN KEY (company_job_id) REFERENCES company_job_postings(job_id)
                    ON DELETE CASCADE
                """)
                connection.commit()
                print("✅ Foreign key constraint added!")
            except Error as e:
                if "Duplicate" in str(e) or "already exists" in str(e):
                    print("ℹ️  Foreign key constraint already exists")
                else:
                    print(f"⚠️  Could not add foreign key: {e}")
        
        # Create index
        print("\n📊 Creating performance index...")
        try:
            cursor.execute("""
                CREATE INDEX idx_opportunities_company_job_id ON opportunities(company_job_id)
            """)
            connection.commit()
            print("✅ Index created")
        except Error as e:
            if "Duplicate key name" in str(e):
                print("ℹ️  Index already exists")
            else:
                print(f"⚠️  Could not create index: {e}")
        
        # Display updated table structure
        print("\n📋 Updated opportunities table structure:")
        cursor.execute("DESCRIBE opportunities")
        columns = cursor.fetchall()
        
        print("\n{:<25} {:<20} {:<10} {:<10}".format("Field", "Type", "Null", "Key"))
        print("-" * 65)
        for col in columns:
            print("{:<25} {:<20} {:<10} {:<10}".format(
                col[0], col[1], col[2], col[3] if col[3] else ''
            ))
        
        print("\n" + "="*65)
        print("🎉 Migration completed successfully!")
        print("="*65)
        
    except Error as e:
        print(f"\n❌ Error: {e}")
        return False
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\n🔌 Database connection closed.")
    
    return True

if __name__ == "__main__":
    print("="*65)
    print("Opportunities Table - Company Job Integration Migration")
    print("="*65)
    add_company_job_integration()
