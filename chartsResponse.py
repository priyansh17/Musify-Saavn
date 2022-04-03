import json

import requests

import endpoints

chartsResponseJSON = {
    "new_albums": [
        {
            "query": "Dasvi",
            "text": "Dasvi",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/165\/Dasvi-Hindi-2022-20220328102530-150x150.jpg",
            "albumid": "33768357",
            "title": "Dasvi",
            "Artist": {
                "music": [
                    {
                        "id": "461968",
                        "name": "Sachin-Jigar"
                    }
                ]
            },
            "weight": 500,
            "language": "hindi"
        },
        {
            "query": "Attack",
            "text": "Attack",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/084\/Attack-Hindi-2022-20220313112514-150x150.jpg",
            "albumid": "33416182",
            "title": "Attack",
            "Artist": {
                "music": [
                    {
                        "id": "2880232",
                        "name": "Shashwat Sachdev"
                    }
                ]
            },
            "weight": 334,
            "language": "hindi"
        },
        {
            "query": "Mast Nazron Se",
            "text": "Mast Nazron Se",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/194\/Mast-Nazron-Se-Hindi-2022-20220331031015-150x150.jpg",
            "albumid": "33910281",
            "title": "Mast Nazron Se",
            "Artist": {
                "music": [
                    {
                        "id": "489732",
                        "name": "Rochak Kohli"
                    },
                    {
                        "id": "881158",
                        "name": "Jubin Nautiyal"
                    },
                    {
                        "id": "891063",
                        "name": "Nasir Iqbal"
                    },
                    {
                        "id": "489732",
                        "name": "Rochak Kohli"
                    },
                    {
                        "id": "489732",
                        "name": "Rochak Kohli"
                    },
                    {
                        "id": "881158",
                        "name": "Jubin Nautiyal"
                    },
                    {
                        "id": "891063",
                        "name": "Nasir Iqbal"
                    }
                ]
            },
            "weight": 250,
            "language": "hindi"
        },
        {
            "query": "Khwaab Khwaab",
            "text": "Khwaab Khwaab",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/630\/Khwaab-Khwaab-Hindi-2022-20220328031001-150x150.jpg",
            "albumid": "33841083",
            "title": "Khwaab Khwaab",
            "Artist": {
                "music": [
                    {
                        "id": "3623110",
                        "name": "Sachet Tandon"
                    },
                    {
                        "id": "3623112",
                        "name": "Sachet-Parampara"
                    },
                    {
                        "id": "3623110",
                        "name": "Sachet Tandon"
                    },
                    {
                        "id": "3623112",
                        "name": "Sachet-Parampara"
                    }
                ]
            },
            "weight": 200,
            "language": "hindi"
        },
        {
            "query": "Ishq Nahi Karte",
            "text": "Ishq Nahi Karte",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/633\/Ishq-Nahi-Karte-Hindi-2022-20220323194638-150x150.jpg",
            "albumid": "33716956",
            "title": "Ishq Nahi Karte",
            "Artist": {
                "music": [
                    {
                        "id": "788130",
                        "name": "B Praak"
                    }
                ]
            },
            "weight": 167,
            "language": "hindi"
        },
        {
            "query": "Rehna Tere Paas",
            "text": "Rehna Tere Paas",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/504\/Rehna-Tere-Paas-Hindi-2022-20220324171937-150x150.jpg",
            "albumid": "33746065",
            "title": "Rehna Tere Paas",
            "Artist": {
                "music": [
                    {
                        "id": "464656",
                        "name": "Armaan Malik"
                    },
                    {
                        "id": "819413",
                        "name": "Anurag Saikia"
                    }
                ]
            },
            "weight": 143,
            "language": "hindi"
        },
        {
            "query": "Kya Kar Diya",
            "text": "Kya Kar Diya",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/042\/Kya-Kar-Diya-Hindi-2022-20220322053603-150x150.jpg",
            "albumid": "33672620",
            "title": "Kya Kar Diya",
            "Artist": {
                "music": [
                    {
                        "id": "702452",
                        "name": "Vishal Mishra"
                    }
                ]
            },
            "weight": 125,
            "language": "hindi"
        },
        {
            "query": "Tera Saath Ho",
            "text": "Tera Saath Ho",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/435\/Tera-Saath-Ho-Hindi-2022-20220324031001-150x150.jpg",
            "albumid": "33728518",
            "title": "Tera Saath Ho",
            "Artist": {
                "music": [
                    {
                        "id": "1595701",
                        "name": "Tanishk Bagchi"
                    },
                    {
                        "id": "712878",
                        "name": "Guru Randhawa"
                    },
                    {
                        "id": "11770594",
                        "name": "Zahrah S Khan"
                    },
                    {
                        "id": "1595701",
                        "name": "Tanishk Bagchi"
                    },
                    {
                        "id": "1595701",
                        "name": "Tanishk Bagchi"
                    },
                    {
                        "id": "1595701",
                        "name": "Tanishk Bagchi"
                    },
                    {
                        "id": "712878",
                        "name": "Guru Randhawa"
                    },
                    {
                        "id": "11770594",
                        "name": "Zahrah S Khan"
                    }
                ]
            },
            "weight": 112,
            "language": "hindi"
        },
        {
            "query": "SAIYAAN",
            "text": "SAIYAAN",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/066\/SAIYAAN-Hindi-2022-20220323183723-150x150.jpg",
            "albumid": "33534703",
            "title": "SAIYAAN",
            "Artist": {
                "music": [
                    {
                        "id": "706985",
                        "name": "Asees Kaur"
                    },
                    {
                        "id": "760994",
                        "name": "Zain"
                    }
                ]
            },
            "weight": 91,
            "language": "hindi"
        },
        {
            "query": "Kya Yehi Pyaar Hai",
            "text": "Kya Yehi Pyaar Hai",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/848\/Kya-Yehi-Pyaar-Hai-Hindi-2022-20220321121019-150x150.jpg",
            "albumid": "33613168",
            "title": "Kya Yehi Pyaar Hai",
            "Artist": {
                "music": [
                    {
                        "id": "743637",
                        "name": "Amaal Mallik"
                    },
                    {
                        "id": "464656",
                        "name": "Armaan Malik"
                    },
                    {
                        "id": "456074",
                        "name": "R.D. Burman"
                    },
                    {
                        "id": "743637",
                        "name": "Amaal Mallik"
                    },
                    {
                        "id": "743637",
                        "name": "Amaal Mallik"
                    },
                    {
                        "id": "464656",
                        "name": "Armaan Malik"
                    },
                    {
                        "id": "456074",
                        "name": "R.D. Burman"
                    }
                ]
            },
            "weight": 84,
            "language": "hindi"
        },
        {
            "query": "The Kashmir Files",
            "text": "The Kashmir Files",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/144\/The-Kashmir-Files-Hindi-2022-20220316121814-150x150.jpg",
            "albumid": "33536564",
            "title": "The Kashmir Files",
            "Artist": {
                "music": [
                    {
                        "id": "455863",
                        "name": "Swapnil Bandodkar"
                    }
                ]
            },
            "weight": 77,
            "language": "hindi"
        },
        {
            "query": "Retropanda - Part 1",
            "text": "Retropanda - Part 1",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/886\/Retropanda-Part-1-Hindi-2022-20220312190528-150x150.jpg",
            "albumid": "33469190",
            "title": "Retropanda - Part 1",
            "Artist": {
                "music": [
                    {
                        "id": "456863",
                        "name": "Badshah"
                    }
                ]
            },
            "weight": 72,
            "language": "hindi"
        },
        {
            "query": "Goriye",
            "text": "Goriye",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/070\/Goriye-Hindi-2022-20220308015542-150x150.jpg",
            "albumid": "33351729",
            "title": "Goriye",
            "Artist": {
                "music": [
                    {
                        "id": "888127",
                        "name": "Darshan Raval"
                    }
                ]
            },
            "weight": 67,
            "language": "hindi"
        },
        {
            "query": "KGF Chapter 2",
            "text": "KGF Chapter 2",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/706\/KGF-Chapter-2-Hindi-2022-20220321173733-150x150.jpg",
            "albumid": "33623338",
            "title": "KGF Chapter 2",
            "Artist": {
                "music": [
                    {
                        "id": "697634",
                        "name": "Ravi Basrur"
                    },
                    {
                        "id": "697634",
                        "name": "Ravi Basrur"
                    }
                ]
            },
            "weight": 63,
            "language": "hindi"
        },
        {
            "query": "Kamle",
            "text": "Kamle",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/252\/Kamle-Hindi-2022-20220314173104-150x150.jpg",
            "albumid": "33496983",
            "title": "Kamle",
            "Artist": {
                "music": [
                    {
                        "id": "2026662",
                        "name": "Akasa"
                    },
                    {
                        "id": "2135738",
                        "name": "Yasser Desai"
                    }
                ]
            },
            "weight": 59,
            "language": "hindi"
        },
        {
            "query": "Sharmaji Namkeen",
            "text": "Sharmaji Namkeen",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/blob\/779\/Sharmaji-Namkeen-Hindi-2022-20220324112535-150x150.jpg",
            "albumid": "33576779",
            "title": "Sharmaji Namkeen",
            "Artist": {
                "music": [
                    {
                        "id": "464289",
                        "name": "Sneha Khanwalkar"
                    }
                ]
            },
            "weight": 53,
            "language": "hindi"
        },
        {
            "query": "Bachchhan Paandey",
            "text": "Bachchhan Paandey",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/491\/Bachchhan-Paandey-Hindi-2022-20220317081001-150x150.jpg",
            "albumid": "33542713",
            "title": "Bachchhan Paandey",
            "Artist": {
                "music": [
                    {
                        "id": "455494",
                        "name": "Various Artists"
                    },
                    {
                        "id": "455494",
                        "name": "Various Artists"
                    }
                ]
            },
            "weight": 50,
            "language": "hindi"
        },
        {
            "query": "Rehn De",
            "text": "Rehn De",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/804\/Rehn-De-Hindi-2022-20220322104437-150x150.jpg",
            "albumid": "33681091",
            "title": "Rehn De",
            "Artist": {
                "music": [
                    {
                        "id": "463007",
                        "name": "Raj Pandit"
                    }
                ]
            },
            "weight": 48,
            "language": "hindi"
        },
        {
            "query": "Kuch Baatein",
            "text": "Kuch Baatein",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/241\/Kuch-Baatein-Hindi-2022-20220310031017-150x150.jpg",
            "albumid": "33406233",
            "title": "Kuch Baatein",
            "Artist": {
                "music": [
                    {
                        "id": "653208",
                        "name": "Payal Dev"
                    },
                    {
                        "id": "881158",
                        "name": "Jubin Nautiyal"
                    },
                    {
                        "id": "653208",
                        "name": "Payal Dev"
                    },
                    {
                        "id": "653208",
                        "name": "Payal Dev"
                    },
                    {
                        "id": "881158",
                        "name": "Jubin Nautiyal"
                    }
                ]
            },
            "weight": 46,
            "language": "hindi"
        },
        {
            "query": "Yaaron Sab Dua Karo",
            "text": "Yaaron Sab Dua Karo",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/095\/Yaaron-Sab-Dua-Karo-Hindi-2022-20220302170632-150x150.jpg",
            "albumid": "33297593",
            "title": "Yaaron Sab Dua Karo",
            "Artist": {
                "music": [
                    {
                        "id": "890048",
                        "name": "Meet Bros"
                    },
                    {
                        "id": "4670197",
                        "name": "Stebin Ben"
                    },
                    {
                        "id": "486204",
                        "name": "Danish Sabri"
                    }
                ]
            },
            "weight": 44,
            "language": "hindi"
        },
        {
            "query": "Mann Basiya",
            "text": "Mann Basiya",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/096\/Mann-Basiya-Hindi-2022-20220315132425-150x150.jpg",
            "albumid": "33516043",
            "title": "Mann Basiya",
            "Artist": {
                "music": [
                    {
                        "id": "711767",
                        "name": "Samira Koppikar"
                    }
                ]
            },
            "weight": 42,
            "language": "hindi"
        },
        {
            "query": "CANDY (Hindi)",
            "text": "CANDY (Hindi)",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/338\/CANDY-Hindi--Hindi-2022-20220228174116-150x150.jpg",
            "albumid": "33106240",
            "title": "CANDY (Hindi)",
            "Artist": {
                "music": [
                    {
                        "id": "456091",
                        "name": "Yuvan Shankar Raja"
                    },
                    {
                        "id": "3623109",
                        "name": "Dhvani Bhanushali"
                    },
                    {
                        "id": "456091",
                        "name": "Yuvan Shankar Raja"
                    }
                ]
            },
            "weight": 39,
            "language": "hindi"
        },
        {
            "query": "The Live-In Song",
            "text": "The Live-In Song",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/304\/The-Live-In-Song-Hindi-2022-20220216151733-150x150.jpg",
            "albumid": "33492571",
            "title": "The Live-In Song",
            "Artist": {
                "music": [
                    {
                        "id": "455124",
                        "name": "Mohit Chauhan"
                    },
                    {
                        "id": "745460",
                        "name": "Nikhita Gandhi"
                    }
                ]
            },
            "weight": 36,
            "language": "hindi"
        },
        {
            "query": "Radhe Shyam",
            "text": "Radhe Shyam",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/323\/Radhe-Shyam-Hindi-2022-20220312141049-150x150.jpg",
            "albumid": "33465586",
            "title": "Radhe Shyam",
            "Artist": {
                "music": [
                    {
                        "id": "702592",
                        "name": "Mithoon"
                    },
                    {
                        "id": "743637",
                        "name": "Amaal Mallik"
                    },
                    {
                        "id": "746774",
                        "name": "Manan Bhardwaj"
                    },
                    {
                        "id": "702592",
                        "name": "Mithoon"
                    },
                    {
                        "id": "743637",
                        "name": "Amaal Mallik"
                    },
                    {
                        "id": "746774",
                        "name": "Manan Bhardwaj"
                    }
                ]
            },
            "weight": 35,
            "language": "hindi"
        },
        {
            "query": "Jhund",
            "text": "Jhund",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/224\/Jhund-Hindi-2022-20220302191001-150x150.jpg",
            "albumid": "33024088",
            "title": "Jhund",
            "Artist": {
                "music": [
                    {
                        "id": "459381",
                        "name": "Ajay-Atul"
                    },
                    {
                        "id": "459381",
                        "name": "Ajay-Atul"
                    }
                ]
            },
            "weight": 34,
            "language": "hindi"
        },
        {
            "query": "Pyaar Hai",
            "text": "Pyaar Hai",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/472\/Pyaar-Hai-Hindi-2022-20220226080203-150x150.jpg",
            "albumid": "33179732",
            "title": "Pyaar Hai",
            "Artist": {
                "music": [
                    {
                        "id": "481520",
                        "name": "Altamash Faridi"
                    },
                    {
                        "id": "653208",
                        "name": "Payal Dev"
                    },
                    {
                        "id": "841827",
                        "name": "Rashmi Virag"
                    },
                    {
                        "id": "653208",
                        "name": "Payal Dev"
                    },
                    {
                        "id": "841827",
                        "name": "Rashmi Virag"
                    },
                    {
                        "id": "481520",
                        "name": "Altamash Faridi"
                    }
                ]
            },
            "weight": 33,
            "language": "hindi"
        },
        {
            "query": "Narazgi",
            "text": "Narazgi",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/079\/Narazgi-Hindi-2022-20220228111858-150x150.jpg",
            "albumid": "33236215",
            "title": "Narazgi",
            "Artist": {
                "music": [
                    {
                        "id": "5902443",
                        "name": "Sonal Pradhan"
                    }
                ]
            },
            "weight": 32,
            "language": "hindi"
        },
        {
            "query": "Lost",
            "text": "Lost",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/404\/Lost-Hindi-2022-20220301053553-150x150.jpg",
            "albumid": "33234519",
            "title": "Lost",
            "Artist": {
                "music": [
                    {
                        "id": "3837440",
                        "name": "Dino James"
                    }
                ]
            },
            "weight": 29,
            "language": "hindi"
        },
        {
            "query": "Teri Ada",
            "text": "Teri Ada",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/756\/Teri-Ada-Hindi-2022-20220215053559-150x150.jpg",
            "albumid": "32904938",
            "title": "Teri Ada",
            "Artist": {
                "music": [
                    {
                        "id": "8875707",
                        "name": "Kaushik-Guddu"
                    },
                    {
                        "id": "455124",
                        "name": "Mohit Chauhan"
                    }
                ]
            },
            "weight": 28,
            "language": "hindi"
        },
        {
            "query": "NAARI",
            "text": "NAARI",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/070\/NAARI-Hindi-2022-20220222125459-150x150.jpg",
            "albumid": "33076968",
            "title": "NAARI",
            "Artist": {
                "music": [
                    {
                        "id": "531639",
                        "name": "Neeti Mohan"
                    }
                ]
            },
            "weight": 28,
            "language": "hindi"
        },
        {
            "query": "Gangubai Kathiawadi",
            "text": "Gangubai Kathiawadi",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/544\/Gangubai-Kathiawadi-Hindi-2022-20220217161339-150x150.jpg",
            "albumid": "32809777",
            "title": "Gangubai Kathiawadi",
            "Artist": {
                "music": [
                    {
                        "id": "464882",
                        "name": "Sanjay Leela Bhansali"
                    },
                    {
                        "id": "464882",
                        "name": "Sanjay Leela Bhansali"
                    }
                ]
            },
            "weight": 27,
            "language": "hindi"
        },
        {
            "query": "Dhokha",
            "text": "Dhokha",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/335\/Dhokha-Hindi-2022-20220210031007-150x150.jpg",
            "albumid": "32799778",
            "title": "Dhokha",
            "Artist": {
                "music": [
                    {
                        "id": "459320",
                        "name": "Arijit Singh"
                    },
                    {
                        "id": "746774",
                        "name": "Manan Bhardwaj"
                    },
                    {
                        "id": "746774",
                        "name": "Manan Bhardwaj"
                    },
                    {
                        "id": "459320",
                        "name": "Arijit Singh"
                    },
                    {
                        "id": "746774",
                        "name": "Manan Bhardwaj"
                    }
                ]
            },
            "weight": 26,
            "language": "hindi"
        },
        {
            "query": "Sharam Lihaaj",
            "text": "Sharam Lihaaj",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/061\/Sharam-Lihaj-Hindi-2022-20220223212400-150x150.jpg",
            "albumid": "33072291",
            "title": "Sharam Lihaaj",
            "Artist": {
                "music": [
                    {
                        "id": "5902443",
                        "name": "Sonal Pradhan"
                    }
                ]
            },
            "weight": 25,
            "language": "hindi"
        },
        {
            "query": "Naina Mere",
            "text": "Naina Mere",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/484\/Naina-Mere-Hindi-2022-20220222131523-150x150.jpg",
            "albumid": "33081153",
            "title": "Naina Mere",
            "Artist": {
                "music": [
                    {
                        "id": "1945909",
                        "name": "Suyyash Rai"
                    },
                    {
                        "id": "7207627",
                        "name": "Anmol Daniel"
                    }
                ]
            },
            "weight": 24,
            "language": "hindi"
        },
        {
            "query": "Wapas Aana To Hai Nahi",
            "text": "Wapas Aana To Hai Nahi",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/070\/Wapas-Aana-To-Hai-Nahi-Hindi-2022-20220216232236-150x150.jpg",
            "albumid": "32954717",
            "title": "Wapas Aana To Hai Nahi",
            "Artist": {
                "music": [
                    {
                        "id": "3535893",
                        "name": "Aniket Shukla"
                    },
                    {
                        "id": "3535893",
                        "name": "Aniket Shukla"
                    },
                    {
                        "id": "745460",
                        "name": "Nikhita Gandhi"
                    },
                    {
                        "id": "3535893",
                        "name": "Aniket Shukla"
                    }
                ]
            },
            "weight": 24,
            "language": "hindi"
        },
        {
            "query": "Insaan",
            "text": "Insaan",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/893\/Insaan-Hindi-2022-20220216154254-150x150.jpg",
            "albumid": "32941062",
            "title": "Insaan",
            "Artist": {
                "music": [
                    {
                        "id": "5889183",
                        "name": "MC STAN"
                    },
                    {
                        "id": "5889183",
                        "name": "MC STAN"
                    },
                    {
                        "id": "5889183",
                        "name": "MC STAN"
                    },
                    {
                        "id": "5889183",
                        "name": "MC STAN"
                    }
                ]
            },
            "weight": 23,
            "language": "hindi"
        },
        {
            "query": "Tum Dill Meinn Ho Mere",
            "text": "Tum Dill Meinn Ho Mere",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/520\/Tum-Dill-Meinn-Ho-Mere-Hindi-2022-20220215103222-150x150.jpg",
            "albumid": "32910765",
            "title": "Tum Dill Meinn Ho Mere",
            "Artist": {
                "music": [
                    {
                        "id": "467309",
                        "name": "Palak Muchhal"
                    },
                    {
                        "id": "455132",
                        "name": "Himesh Reshammiya"
                    }
                ]
            },
            "weight": 23,
            "language": "hindi"
        },
        {
            "query": "Love Hostel",
            "text": "Love Hostel",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/036\/Love-Hostel-Hindi-2022-20220228152055-150x150.jpg",
            "albumid": "33054784",
            "title": "Love Hostel",
            "Artist": {
                "music": [
                    {
                        "id": "464912",
                        "name": "Jeet Gannguli"
                    },
                    {
                        "id": "4668770",
                        "name": "Shor Police"
                    },
                    {
                        "id": "456051",
                        "name": "Clinton Cerejo"
                    }
                ]
            },
            "weight": 22,
            "language": "hindi"
        },
        {
            "query": "Mud Mud Ke",
            "text": "Mud Mud Ke",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/183\/Mud-Mud-Ke-Hindi-2022-20220205115120-150x150.jpg",
            "albumid": "32689884",
            "title": "Mud Mud Ke",
            "Artist": {
                "music": [
                    {
                        "id": "455917",
                        "name": "Tony Kakkar"
                    },
                    {
                        "id": "455917",
                        "name": "Tony Kakkar"
                    },
                    {
                        "id": "455917",
                        "name": "Tony Kakkar"
                    },
                    {
                        "id": "464932",
                        "name": "Neha Kakkar"
                    }
                ]
            },
            "weight": 22,
            "language": "hindi"
        },
        {
            "query": "Gehraiyaan (Original Motion Picture Soundtrack)",
            "text": "Gehraiyaan (Original Motion Picture Soundtrack)",
            "year": "2022",
            "image": "https:\/\/c.saavncdn.com\/084\/Gehraiyaan-Original-Motion-Picture-Soundtrack--Hindi-2022-20220206184958-150x150.jpg",
            "albumid": "32712499",
            "title": "Gehraiyaan (Original Motion Picture Soundtrack)",
            "Artist": {
                "music": [
                    {
                        "id": "5609542",
                        "name": "OAFF"
                    },
                    {
                        "id": "1752043",
                        "name": "Savera"
                    }
                ]
            },
            "weight": 21,
            "language": "hindi"
        }
    ],
    "featured_playlists": [
        {
            "listid": "5424",
            "firstname": "JioSaavn",
            "listname": "Surprise Me",
            "data_type": "random",
            "count": 20,
            "image": "https:\/\/pli.saavncdn.com\/54\/24\/5424.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/surprise-me\/1ZOczFTRyFw_",
            "follower_count": "2318",
            "uid": "phulki_user",
            "last_updated": 1525086300
        },
        {
            "listid": "1367823",
            "firstname": "JioSaavn",
            "listname": "Melodious Hariharan",
            "data_type": "featured",
            "count": 34,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/MelodiousHariharan_20190329072337.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/melodious-hariharan\/fqAzQOJ-e9M_",
            "follower_count": "2495",
            "uid": "phulki_user",
            "last_updated": 1648881673
        },
        {
            "listid": "49",
            "firstname": "JioSaavn",
            "listname": "Weekly Top Songs",
            "data_type": "weekly",
            "count": 48,
            "image": "https:\/\/c.saavncdn.com\/editorial\/wt15-49_20220401120056.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/weekly-top-songs\/8MT-LQlP35c_",
            "follower_count": "2249650",
            "uid": "phulki_user",
            "last_updated": 1648778486
        },
        {
            "listid": "158203462",
            "firstname": "JioSaavn",
            "listname": "At The Box Office",
            "data_type": "featured",
            "count": 14,
            "image": "https:\/\/c.saavncdn.com\/editorial\/AtTheBoxOffice_20220331180851.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/at-the-box-office\/VGYtuNra07Lc1EngHtQQ2g__",
            "follower_count": "49018",
            "uid": "phulki_user",
            "last_updated": 1648714484
        },
        {
            "listid": "756986959",
            "firstname": "JioSaavn",
            "listname": "Retro Duets - Hindi",
            "data_type": "featured",
            "count": 20,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/RetroDuetsHindi_20200227075146.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/retro-duets---hindi\/rQ4mVdrdGE,O0eMLZZxqsA__",
            "follower_count": "6764",
            "uid": "phulki_user",
            "last_updated": 1582750328
        },
        {
            "listid": "72903410",
            "firstname": "JioSaavn",
            "listname": "Sirf Unplugged",
            "data_type": "featured",
            "count": 25,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/Unplugged_20220110155848.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/sirf-unplugged\/QkY0PeqdTW4_",
            "follower_count": "58845",
            "uid": "phulki_user",
            "last_updated": 1641790764
        },
        {
            "listid": "1042909247",
            "firstname": "JioSaavn",
            "listname": "Nach Le - With Ajay Devgn - Hindi",
            "data_type": "featured",
            "count": 25,
            "image": "https:\/\/c.saavncdn.com\/editorial\/NachLeWithAjayDevgnHindi_20220330145441.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/nach-le---with-ajay-devgn---hindi\/BUsNxwErfornZqie6EVsAw__",
            "follower_count": "36",
            "uid": "phulki_user",
            "last_updated": 1648616734
        },
        {
            "listid": "159910141",
            "firstname": "JioSaavn",
            "listname": "DeSHE Hip Hop",
            "data_type": "featured",
            "count": 19,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/DeSHEHipHop_20211209165048.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/deshe-hip-hop\/3HDqp7oOhzwGSw2I1RxdhQ__",
            "follower_count": "482",
            "uid": "phulki_user",
            "last_updated": 1647459805
        },
        {
            "listid": "81883575",
            "firstname": "JioSaavn",
            "listname": "Tiger Ki Heropanti",
            "data_type": "featured",
            "count": 24,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/TigerKiHeropanti_20210810022912.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/tiger-ki-heropanti\/3N4MvOxhc04_",
            "follower_count": "12963",
            "uid": "phulki_user",
            "last_updated": 1648755764
        },
        {
            "listid": "30846843",
            "firstname": "JioSaavn",
            "listname": "Kishore - Funny Side Up",
            "data_type": "featured",
            "count": 15,
            "image": "https:\/\/c.saavncdn.com\/editorial\/KishoreFunnySideUp_20220311191313.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/kishore---funny-side-up\/KbkjktWEeKk_",
            "follower_count": "8408",
            "uid": "phulki_user",
            "last_updated": 1646986569
        },
        {
            "listid": "110470443",
            "firstname": "JioSaavn",
            "listname": "Musical Jodis - Sachin-Jigar",
            "data_type": "featured",
            "count": 62,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/MusicalJodisSachinJigar_20210304180912.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/musical-jodis---sachin-jigar\/43nsk2Qd948wkg5tVhI3fw__",
            "follower_count": "905",
            "uid": "phulki_user",
            "last_updated": 1648413506
        },
        {
            "listid": "940775963",
            "firstname": "JioSaavn",
            "listname": "Best Of Indipop - Hindi",
            "data_type": "featured",
            "count": 30,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/BestOfIndipopHindi_20210622173011.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/best-of-indipop---hindi\/xHa-oM3ldXAwkg5tVhI3fw__",
            "follower_count": "4837",
            "uid": "phulki_user",
            "last_updated": 1625904695
        },
        {
            "listid": "829470829",
            "firstname": "JioSaavn",
            "listname": "Decade Of Heroines - 1990s",
            "data_type": "featured",
            "count": 20,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/DecadeOfHeroines1990s_20210824153137.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/decade-of-heroines---1990s\/eggAXNMLX6GO0eMLZZxqsA__",
            "follower_count": "4887",
            "uid": "phulki_user",
            "last_updated": 1636957975
        },
        {
            "listid": "938512501",
            "firstname": "JioSaavn",
            "listname": "Editor's Pick - Hindi",
            "data_type": "featured",
            "count": 19,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/Editor_sPickHindi_20220119071238.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/editors-pick---hindi\/8J5ACBCJtgcGSw2I1RxdhQ__",
            "follower_count": "350",
            "uid": "phulki_user",
            "last_updated": 1648590766
        },
        {
            "listid": "83421839",
            "firstname": "JioSaavn",
            "listname": "Ishqiyaan",
            "data_type": "featured",
            "count": 25,
            "image": "https:\/\/c.saavncdn.com\/editorial\/Ishqiyaan_20220331180832.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/ishqiyaan\/dyqSeSlJrvI_",
            "follower_count": "523096",
            "uid": "phulki_user",
            "last_updated": 1648755871
        },
        {
            "listid": "757656308",
            "firstname": "JioSaavn",
            "listname": "2000s Duets - Hindi",
            "data_type": "featured",
            "count": 20,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/2000sDuets_20211203161917.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/2000s-duets---hindi\/NaV3HkhAB5FFo9wdEAzFBA__",
            "follower_count": "44491",
            "uid": "phulki_user",
            "last_updated": 1638508788
        },
        {
            "listid": "6689255",
            "firstname": "JioSaavn",
            "listname": "Taaza Tunes",
            "data_type": "featured",
            "count": 35,
            "image": "https:\/\/c.saavncdn.com\/editorial\/TaazaTunes_20220401062650.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/taaza-tunes\/Me5RridRfDk_",
            "follower_count": "523309",
            "uid": "phulki_user",
            "last_updated": 1648758608
        },
        {
            "listid": "944826465",
            "firstname": "JioSaavn",
            "listname": "Remake Hits 2021 - Hindi",
            "data_type": "featured",
            "count": 22,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/RemakeHits2021Hindi_20211201161048.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/remake-hits-2021---hindi\/3iC0jfyxNVjuCJW60TJk1Q__",
            "follower_count": "22000",
            "uid": "phulki_user",
            "last_updated": 1638805876
        },
        {
            "listid": "5148894",
            "firstname": "JioSaavn",
            "listname": "Nach Le",
            "data_type": "featured",
            "count": 20,
            "image": "https:\/\/c.saavncdn.com\/editorial\/NachLe_20220326074539.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/nach-le\/UQjTO6rFZfc_",
            "follower_count": "504948",
            "uid": "phulki_user",
            "last_updated": 1648604145
        },
        {
            "listid": "330056058",
            "firstname": "JioSaavn",
            "listname": "Desi Rock",
            "data_type": "featured",
            "count": 19,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/DesiRockSongs_20210120154545.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/desi-rock\/DGl4UBWnRqlFo9wdEAzFBA__",
            "follower_count": "16327",
            "uid": "phulki_user",
            "last_updated": 1643571010
        },
        {
            "listid": "156473621",
            "firstname": "JioSaavn",
            "listname": "Pop Mein Top",
            "data_type": "featured",
            "count": 25,
            "image": "https:\/\/c.saavncdn.com\/editorial\/PopMeinTop_20220324082625.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/pop-mein-top\/pDQtHvJRh4IGSw2I1RxdhQ__",
            "follower_count": "217093",
            "uid": "phulki_user",
            "last_updated": 1648758044
        },
        {
            "listid": "81169121",
            "firstname": "JioSaavn",
            "listname": "Junior Bachchan - Right Here Right Now",
            "data_type": "featured",
            "count": 32,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/JuniorBachchanRightHereRightNow_20210120154625.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/junior-bachchan---right-here-right-now\/ZnqIAerDW8Q_",
            "follower_count": "6003",
            "uid": "phulki_user",
            "last_updated": 1648154527
        },
        {
            "listid": "100294896",
            "firstname": "JioSaavn",
            "listname": "Desi Hip Hop",
            "data_type": "featured",
            "count": 50,
            "image": "https:\/\/c.saavncdn.com\/editorial\/DesiHipHop_20220326084044.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/desi-hip-hop\/xc1PuFo0lwHfemJ68FuXsA__",
            "follower_count": "12170",
            "uid": "phulki_user",
            "last_updated": 1648248148
        },
        {
            "listid": "85730158",
            "firstname": "JioSaavn",
            "listname": "Shining Star - Armaan Malik",
            "data_type": "featured",
            "count": 47,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/ShiningStarArmaanMalik_20210112170408.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/shining-star---armaan-malik\/UKM0ht9,MIc_",
            "follower_count": "20880",
            "uid": "phulki_user",
            "last_updated": 1648141361
        },
        {
            "listid": "804316688",
            "firstname": "JioSaavn",
            "listname": "Hindi EDM",
            "data_type": "featured",
            "count": 22,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/HindiEDM_20211112084227.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/hindi-edm\/OYy8Eam-WpZFo9wdEAzFBA__",
            "follower_count": "7888",
            "uid": "phulki_user",
            "last_updated": 1648413556
        },
        {
            "listid": "1020129788",
            "firstname": "JioSaavn",
            "listname": "Men In Indipop: New Hits",
            "data_type": "featured",
            "count": 20,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/MenInIndipop-NewHits_20220107163215.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/men-in-indipop:-new-hits\/Bxu4BRUH9dXDN85e-DKVsA__",
            "follower_count": "6604",
            "uid": "phulki_user",
            "last_updated": 1648142880
        },
        {
            "listid": "5519117",
            "firstname": "JioSaavn",
            "listname": "Rahmania",
            "data_type": "featured",
            "count": 82,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/Rahmania_20201222164204.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/rahmania\/8,4hXFdAgZc_",
            "follower_count": "22574",
            "uid": "phulki_user",
            "last_updated": 1648755778
        },
        {
            "listid": "66034298",
            "firstname": "JioSaavn",
            "listname": "Rap Ka Badshah",
            "data_type": "featured",
            "count": 59,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/RapKaBadshah_20201110163731.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/rap-ka-badshah\/JKy,RYg3-xI_",
            "follower_count": "117557",
            "uid": "phulki_user",
            "last_updated": 1648069999
        },
        {
            "listid": "82650564",
            "firstname": "JioSaavn",
            "listname": "Emraan Hashmi - Phir Mohabbat",
            "data_type": "featured",
            "count": 32,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/EmraanHashmiPhirMohabbat_20210304180830.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/emraan-hashmi---phir-mohabbat\/CLpr-AvsCdg_",
            "follower_count": "98593",
            "uid": "phulki_user",
            "last_updated": 1648065183
        },
        {
            "listid": "107605145",
            "firstname": "JioSaavn",
            "listname": "Indiependent India - Desi Pop",
            "data_type": "featured",
            "count": 50,
            "image": "https:\/\/c.saavncdn.com\/editorial\/logo\/IndiependentIndiaDesiPop_20220212164715.jpg",
            "sponsored": "false",
            "perma_url": "https:\/\/www.jiosaavn.com\/featured\/indiependent-india---desi-pop\/jnjK2XTv9-3uCJW60TJk1Q__",
            "follower_count": "3566",
            "uid": "phulki_user",
            "last_updated": 1648758189
        }
    ],
    "user_state": {
        "user_logged_in": 0,
        "free_stream_limit": 200,
        "free_stream_counter": 0,
        "free_downloads_enabled": "false"
    },
    "global_config": {
        "spotlight_image_width": "320",
        "spotlight_image_height": "86",
        "spotlight_image_expiry": "0",
        "spotlight_view_image_width": "320",
        "spotlight_view_image_height": "86",
        "spotlight_view_image_expiry": "0",
        "spotlight_image": "http:\/\/s.saavncdn.com\/apps\/spotlight\/img\/HP-1-201404251512.jpg",
        "spotlight_view_image": "http:\/\/s.saavncdn.com\/apps\/spotlight\/img\/HP-2-201404251512.jpg",
        "spotlight_movie_acronym": "HP",
        "spotlight_action": "PLAYLIST_SHOW",
        "spotlight_content": "9931259",
        "spotlight_content_name": "CGE Rahul Vaidya",
        "spotlight_view_action": "PLAYLIST_PLAY",
        "spotlight_view_content": "9931259",
        "connection_timeout": 60000,
        "socket_timeout": 60000,
        "song_object_version": "1.0",
        "stream_config": {
            "available_bitrates": [
                "320",
                "160",
                "96",
                "48",
                "12"
            ],
            "bitrates_map": {
                "320": {
                    "name": "Super Duper High",
                    "code": 1
                },
                "160": {
                    "name": "Really High",
                    "code": 2
                },
                "96": {
                    "name": "Pretty High",
                    "code": 3
                },
                "48": {
                    "name": "Less High",
                    "code": 4
                },
                "12": {
                    "name": "Sorta High...ish?",
                    "code": 5
                }
            },
            "bitrate": {
                "2g": 12,
                "3g": 48,
                "4g": 96
            }
        },
        "notification_duration": 10000,
        "ad_config": {
            "networks": [
                "dfp",
                "inmobi",
                "admob"
            ]
        },
        "supported_languages": [
            "hindi",
            "english",
            "tamil",
            "telugu",
            "punjabi",
            "marathi",
            "gujarati",
            "bengali",
            "kannada",
            "bhojpuri",
            "malayalam",
            "urdu",
            "haryanvi",
            "rajasthani",
            "odia",
            "assamese"
        ],
        "radio_supported_languages": [
            "hindi",
            "english",
            "tamil",
            "telugu",
            "kannada",
            "punjabi",
            "marathi",
            "malayalam"
        ],
        "af_enabled": "true",
        "cf_enabled": "false",
        "weekly_top_songs_listid": "49",
        "random_songs_listid": "5424"
    },
    "charts": [
        {
            "listid": "110858205",
            "listname": "Trending Today",
            "image": "https://c.saavncdn.com/editorial/charts_TrendingToday_149406_20220319164713.jpg",
            "weight": 1000,
            "songs": [
                {
                    "name": "Kudiyan Lahore Diyan",
                    "image": "http://c.saavncdn.com/771/Kudiyan-Lahore-Diyan-Punjabi-2022-20220328053542-150x150.jpg"
                },
                {
                    "name": "Chandra (Featuring. Shreya Ghoshal)",
                    "image": "http://c.saavncdn.com/771/Chandramukhi-Marathi-2022-20220329193225-150x150.jpg"
                },
                {
                    "name": "Korbo Lorbo Jeetbo",
                    "image": "http://c.saavncdn.com/513/Korbo-Lorbo-Jeetbo-Single-Hindi-2016-150x150.jpg"
                },
                {
                    "name": "Kajwa",
                    "image": "http://c.saavncdn.com/246/Kajwa-Marathi-2022-20220201124047-150x150.jpg"
                },
                {
                    "name": "Pasoori",
                    "image": "http://c.saavncdn.com/663/Pasoori-Punjabi-2022-20220203181058-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"
        },
        {
            "listid": "848372055",
            "listname": "Hindi Chartbusters",
            "image": "https://c.saavncdn.com/editorial/charts_HindiChartbusters_158236_20220311194231.jpg",
            "weight": 500,
            "songs": [
                {
                    "name": "Dhokha",
                    "image": "http://c.saavncdn.com/335/Dhokha-Hindi-2022-20220210031007-150x150.jpg"
                },
                {
                    "name": "Pyaar Karte Ho Na",
                    "image": "http://c.saavncdn.com/150/Pyaar-Karte-Ho-Na-Hindi-2021-20211123053301-150x150.jpg"
                },
                {
                    "name": "Raataan Lambiyan",
                    "image": "http://c.saavncdn.com/238/Shershaah-Original-Motion-Picture-Soundtrack--Hindi-2021-20210815181610-150x150.jpg"
                },
                {
                    "name": "Dil Galti Kar Baitha Hai (Feat. Mouni Roy)",
                    "image": "http://c.saavncdn.com/279/Dil-Galti-Kar-Baitha-Hai-Feat-Mouni-Roy--Hindi-2021-20210924182700-150x150.jpg"
                },
                {
                    "name": "Thoda Thoda Pyaar",
                    "image": "http://c.saavncdn.com/959/Thoda-Thoda-Pyaar-Hindi-2021-20210212084501-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_chartbusters/1HiqW,xnqZTuCJW60TJk1Q__"
        },
        {
            "listid": "142311984",
            "listname": "Romantic Top 40",
            "image": "https://c.saavncdn.com/editorial/charts_RomanticTop40_167985_20220311173413.jpg",
            "weight": 334,
            "songs": [
                {
                    "name": "Dhokha",
                    "image": "http://c.saavncdn.com/335/Dhokha-Hindi-2022-20220210031007-150x150.jpg"
                },
                {
                    "name": "Pyaar Karte Ho Na",
                    "image": "http://c.saavncdn.com/150/Pyaar-Karte-Ho-Na-Hindi-2021-20211123053301-150x150.jpg"
                },
                {
                    "name": "Maiyya Mainu",
                    "image": "http://c.saavncdn.com/799/Jersey-Hindi-2021-20211224123053-150x150.jpg"
                },
                {
                    "name": "Meri Zindagi Hai Tu (From &quot;Satyameva Jayate 2&quot;)",
                    "image": "http://c.saavncdn.com/731/Meri-Zindagi-Hai-Tu-From-Satyameva-Jayate-2--Hindi-2021-20211028031002-150x150.jpg"
                },
                {
                    "name": "Suna Hai",
                    "image": "http://c.saavncdn.com/597/Sanak-Hindi-2021-20211012105203-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/romantic_top_40/m9Qkal5S733ufxkxMEIbIw__"
        },
        {
            "listid": "48147819",
            "listname": "Hindi 00s",
            "image": "https://c.saavncdn.com/editorial/logo/charts_Hindi00s_122250_20190906160607.jpg",
            "weight": 250,
            "songs": [
                {
                    "name": "Tere Naam",
                    "image": "http://c.saavncdn.com/516/Tere-Naam-Hindi-2003-150x150.jpg"
                },
                {
                    "name": "Dil Ne Yeh Kaha Hain Dil Se",
                    "image": "http://c.saavncdn.com/454/Dhadkan-Hindi-2000-20210226131403-150x150.jpg"
                },
                {
                    "name": "Woh Lamhein",
                    "image": "http://c.saavncdn.com/932/Zeher-Hindi-2005-20180115-150x150.jpg"
                },
                {
                    "name": "Zara Sa",
                    "image": "http://c.saavncdn.com/801/Jannat-Hindi-2008-20190629135803-150x150.jpg"
                },
                {
                    "name": "Chand Sifarish",
                    "image": "http://c.saavncdn.com/146/Fanaa-Hindi-2006-20190329181154-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_00s/tsJahdem34A_"
        },
        {
            "listid": "48147816",
            "listname": "Hindi 90s",
            "image": "https://c.saavncdn.com/editorial/logo/charts_Hindi90s_142072_20190906160631.jpg",
            "weight": 200,
            "songs": [
                {
                    "name": "Tujhe Dekha To",
                    "image": "http://c.saavncdn.com/588/Dilwale-Dulhania-Le-Jayenge-Hindi-1995-20171114-150x150.jpg"
                },
                {
                    "name": "Mera Dil Bhi Kitna Pagal Hai",
                    "image": "http://c.saavncdn.com/461/Saajan-Hindi-1991-20210407065213-150x150.jpg"
                },
                {
                    "name": "Dheere Dheere Se Meri Zindagi Mein Aana",
                    "image": "http://c.saavncdn.com/365/Aashiqui-Hindi-1989-150x150.jpg"
                },
                {
                    "name": "Dil To Pagal Hai",
                    "image": "http://c.saavncdn.com/410/Dil-To-Pagal-Hai-Hindi-1997-20190329145756-150x150.jpg"
                },
                {
                    "name": "Tumhein Apna Banane Ki Kasam Khai Hai",
                    "image": "http://c.saavncdn.com/020/Sadak-Hindi-1991-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_90s/T64MUCqdndw_"
        },
        {
            "listid": "82712615",
            "listname": "Hindi 80s",
            "image": "https://c.saavncdn.com/editorial/logo/charts_Hindi80s_108023_20220105060041.jpg",
            "weight": 167,
            "songs": [
                {
                    "name": "Hazaar Raahen",
                    "image": "http://c.saavncdn.com/content/1/album/Y/YWQ5ZjE1YTc5NDNlMjVmOGExYmIxNDVjYTcxYTI4NjY_-thumb.jpg"
                },
                {
                    "name": "Shisha-Ho-Ya-Dil-Ho---Lata-Mangeshkar",
                    "image": "http://c.saavncdn.com/content/5/album/Y/Y2JjMTZkOTI3YmRmOWI2NDRhYWEzZmE1ODEzYjIzMTU_-thumb.jpg"
                },
                {
                    "name": "Dil Cheez Kya Hai",
                    "image": "http://c.saavncdn.com/599/Umrao-Jaan-1981-150x150.jpg"
                },
                {
                    "name": "Phir Chiddi Raat",
                    "image": "http://c.saavncdn.com/847/Bazaar-1981-150x150.jpg"
                },
                {
                    "name": "Raat Baaqi Baat Baaqi",
                    "image": "http://c.saavncdn.com/243/Namak-Halaal-Hindi-1982-20220211160823-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_80s/fE9YxTvTDjU_"
        },
        {
            "listid": "82712414",
            "listname": "Hindi 70s",
            "image": "https://c.saavncdn.com/editorial/logo/charts_Hindi70s_119337_20220105060121.jpg",
            "weight": 143,
            "songs": [
                {
                    "name": "Ek Ajnabee Haseena Se",
                    "image": "http://c.saavncdn.com/721/Ajanabee-1974-150x150.jpg"
                },
                {
                    "name": "Chabi Kho Jayi - Hum Tum Ek Kamre Mein",
                    "image": "http://c.saavncdn.com/059/Bobby-Hindi-1973-20200901173923-150x150.jpg"
                },
                {
                    "name": "Tere Bina Zindagi Se",
                    "image": "http://c.saavncdn.com/292/Aandhi-Hindi-1975-20200905113925-150x150.jpg"
                },
                {
                    "name": "Kabhi Kabhi Mere Dil Mein Duet",
                    "image": "http://c.saavncdn.com/293/Kabhi-Kabhie-Hindi-1976-20200901153954-150x150.jpg"
                },
                {
                    "name": "Aap Ki Ankhon Mein Kuch",
                    "image": "http://c.saavncdn.com/784/Ghar-Hindi-1978-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_70s/VSMrnr-njCk_"
        },
        {
            "listid": "82711924",
            "listname": "Hindi 60s",
            "image": "https://c.saavncdn.com/editorial/logo/charts_Hindi60s_124027_20220105060140.jpg",
            "weight": 125,
            "songs": [
                {
                    "name": "Abhi Na Jao Chhod Kar",
                    "image": "http://c.saavncdn.com/045/Hum-Dono-Hindi-1961-150x150.jpg"
                },
                {
                    "name": "O Haseena Zulfonwale Jane Jahan",
                    "image": "http://c.saavncdn.com/925/Teesri-Manzil-Hindi-1966-150x150.jpg"
                },
                {
                    "name": "Bekhudi Mein Sanam",
                    "image": "http://c.saavncdn.com/428/Hasina-Maan-Jayegi-Hindi-1968-20190220-150x150.jpg"
                },
                {
                    "name": "An Evening In Paris",
                    "image": "http://c.saavncdn.com/413/An-Evening-In-Paris-1967-150x150.jpg"
                },
                {
                    "name": "Kora Kagaz Tha Yeh Man Mera",
                    "image": "http://c.saavncdn.com/951/Aradhana-Hindi-1969-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_60s/TOL5Rewc8Mk_"
        },
        {
            "listid": "82711913",
            "listname": "Hindi Retro",
            "image": "https://c.saavncdn.com/editorial/charts_HindiRetro_157266_20220311175017.jpg",
            "weight": 112,
            "songs": [
                {
                    "name": "Leke Pahla Pahla Pyar",
                    "image": "http://c.saavncdn.com/215/C-I-D-Hindi-1956-20170914050654-150x150.jpg"
                },
                {
                    "name": "Mang Ke Saath Tumhara",
                    "image": "http://c.saavncdn.com/552/Naya-Daur-Hindi-1957-20211213144646-150x150.jpg"
                },
                {
                    "name": "Hai Apna Dil To Aawara (Happy)",
                    "image": "http://c.saavncdn.com/content/1/album/N/NjhlNjBlMzgzNDIxYjRjNThhZmUxZjU1YTI4ZDRkNjc_-thumb.jpg"
                },
                {
                    "name": "Sar Jo Tera Chakraye",
                    "image": "http://c.saavncdn.com/456/Pyaasa-2004-150x150.jpg"
                },
                {
                    "name": "Pyar Hua Iqrar Hua",
                    "image": "http://c.saavncdn.com/443/Shree-420-1955-150x150.jpg"
                }
            ],
            "perma_url": "https://www.jiosaavn.com/featured/hindi_retro/dYn-,-QcKzA_"
        }
    ],
    "genres": [
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Party.jpg",
            "title": "Party",
            "tags": "Party",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Workout.jpg",
            "title": "Workout",
            "tags": "Workout",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Bhangra.jpg",
            "title": "Bhangra",
            "tags": "Bhangra",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Chill.jpg",
            "title": "Chill",
            "tags": "Soft",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Classics.jpg",
            "title": "Classics",
            "tags": "Oldies",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Devotional.jpg",
            "title": "Devotional",
            "tags": "Devotional",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Garba.jpg",
            "title": "Garba",
            "tags": " Garba",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Ghazals.jpg",
            "title": "Ghazals",
            "tags": " Ghazal ",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Instrumental.jpg",
            "title": "Instrumental",
            "tags": "Instrumental",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Live.jpg",
            "title": "Live",
            "tags": "Live ",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Pop.jpg",
            "title": "Pop",
            "tags": "Pop",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Remixes.jpg",
            "title": "Remixes",
            "tags": "Remixes",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Rock.jpg",
            "title": "Rock",
            "tags": "Rock ",
            "about": ""
        },
        {
            "image": "https:\/\/c.saavncdn.com\/editorial\/genrecharts_Sufi.jpg",
            "title": "Sufi",
            "tags": "Sufi",
            "about": ""
        }
    ]
}


def getCharts():
    search_base_url = endpoints.homepage_url
    response = requests.get(search_base_url).text.encode()
    response = json.loads(response)
    getChartsList = []
    if len(response['charts']) == 0:
        allCharts = chartsResponseJSON['charts']
    else:
        allCharts = response['charts']
    for chart in allCharts:
        tempDict = {'topic': chart['listname'], 'urlTopicImage': chart['image'], 'songs': chart['songs']}
        getChartsList.append(tempDict)
    return json.dumps(getChartsList)
