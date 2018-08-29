# Parse XML document/data
import xml.etree.ElementTree as ET

# Multi-line string data
data = '''  
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>   
    '''

# Parse the string from data
tree = ET.fromstring(data)

# Print results
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text)
print('Attributes:', tree.find('email').get('hide'))


# Multiple tags
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(input)
lst = tree.findall('users/user')  # list of tags
print('Users count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))