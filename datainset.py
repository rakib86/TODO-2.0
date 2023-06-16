try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()
    
    
    try:
    with conn.cursor() as cursor:
        # Delete a record
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Commit changes
    conn.commit()

    print("Record deleted successfully")
finally:
    conn.close()
    try:
    with conn.cursor() as cursor:
        # Update a record
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Commit changes
    conn.commit()

    print("Record updated successfully")
finally:
    conn.close()
    try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()
    
    
    try:
    with conn.cursor() as cursor:
        # Delete a record
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Commit changes
    conn.commit()

    print("Record deleted successfully")
finally:
    conn.close()
    try:
    with conn.cursor() as cursor:
        # Update a record
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Commit changes
    conn.commit()

    print("Record updated successfully")
finally:
    conn.close()
    try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    print("Record inserted successfully")
finally:
    conn.close()
    
    
    try:
    with conn.cursor() as cursor:
        # Delete a record
        sql = "DELETE FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('john@example.com',))

    # Commit changes
    conn.commit()

    print("Record deleted successfully")
finally:
    conn.close()
    try:
    with conn.cursor() as cursor:
        # Update a record
        sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
        cursor.execute(sql, ('newpassword', 'john@example.com'))

    # Commit changes
    conn.commit()

    print("Record updated successfully")
finally:
    conn.close()