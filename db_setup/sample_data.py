# Replicated data (same across all 3 DBs)
REPLICATED_BRANDS = [
    ('Sony', 'Japan', 1946),
    ('Nikon', 'Japan', 1917),
    ('Canon', 'Japan', 1937),
    ('Fujifilm', 'Japan', 1934),
    ('Panasonic', 'Japan', 1918),
    ('Olympus', 'Japan', 1919),
    ('Leica', 'Germany', 1914),
    ('Pentax', 'Japan', 1919),
    ('Hasselblad', 'Sweden', 1841),
    ('Phase One', 'Denmark', 1993),
]

REPLICATED_CAMERA_TYPES = [
    ('DSLR', 'Digital Single-Lens Reflex'),
    ('Mirrorless', 'Compact mirrorless system'),
    ('Cinema', 'Professional cinema camera'),
    ('Medium Format', 'Larger sensor format'),
    ('Point and Shoot', 'Compact camera'),
    ('Action Camera', 'Compact rugged camera for sports'),
    ('Instant Camera', 'Instant film photography'),
    ('Film Camera', 'Traditional film-based camera'),
    ('Rangefinder', 'Manual focus with rangefinder mechanism'),
    ('Box Camera', 'Large format studio camera'),
]

# DB1 (Sony, Hasselblad, Canon) data
DB1_CAMERAS = [
    (1, 2, 'Sony A7 IV', 2021, 2499.99),
    (1, 2, 'Sony A7R V', 2022, 3899.99),
    (1, 3, 'Sony FX3', 2021, 3899.99),
    (9, 4, 'Hasselblad X2D 100C', 2022, 8199.00),
    (9, 4, 'Hasselblad 907X 50C', 2019, 5750.00),
    (3, 2, 'Canon EOS R5', 2020, 3899.00),
    (3, 2, 'Canon EOS R6 Mark II', 2022, 2499.00),
    (1, 2, 'Sony A7 III', 2018, 1999.99),
    (3, 1, 'Canon EOS 5D Mark IV', 2016, 2499.00),
    (1, 2, 'Sony A1', 2021, 6499.99),
]

DB1_LENSES = [
    (1, '24-70mm', 'f/2.8', 'Zoom', 2199.99),
    (1, '50mm', 'f/1.2', 'Prime', 1999.99),
    (1, '85mm', 'f/1.4', 'Portrait', 1799.99),
    (1, '35mm', 'f/1.4', 'Prime', 1398.00),
    (9, '90mm', 'f/3.2', 'Portrait', 1899.00),
    (9, '38mm', 'f/2.5', 'Prime', 999.00),
    (3, '24-105mm', 'f/4', 'Zoom', 1099.00),
    (3, '85mm', 'f/1.2', 'Portrait', 2699.00),
    (3, '16-35mm', 'f/2.8', 'Wide Angle', 2299.00),
    (1, '200-600mm', 'f/5.6-6.3', 'Super Telephoto', 1998.00),
]

DB1_ACCESSORIES = [
    ('Sony VG-C4EM Grip', 'Battery Grip', 348.00, 'Sony'),
    ('Sony NP-FZ100 Battery', 'Battery', 78.00, 'Sony'),
    ('Sony ECM-B1M Microphone', 'Microphone', 348.00, 'Sony'),
    ('Sony FDA-EP18 Eyecup', 'Eyecup', 18.00, 'Sony'),
    ('Hasselblad Battery Grip', 'Battery Grip', 549.00, 'Hasselblad'),
    ('Hasselblad Rechargeable Battery', 'Battery', 149.00, 'Hasselblad'),
    ('Canon BG-R10 Grip', 'Battery Grip', 349.00, 'Canon'),
    ('Canon LP-E6NH Battery', 'Battery', 79.00, 'Canon'),
    ('Canon Speedlite 600EX II-RT', 'Flash', 569.00, 'Canon'),
    ('Peak Design Strap', 'Camera Strap', 64.95, 'All Brands'),
]

# DB2 (Nikon, Fujifilm, Panasonic) data
DB2_CAMERAS = [
    (2, 1, 'Nikon D850', 2017, 2996.95),
    (2, 2, 'Nikon Z9', 2021, 5496.95),
    (2, 2, 'Nikon Z6 III', 2024, 2499.95),
    (2, 1, 'Nikon D780', 2020, 2296.95),
    (4, 2, 'Fujifilm X-T5', 2022, 1699.00),
    (4, 4, 'Fujifilm GFX 100S', 2021, 5999.00),
    (4, 2, 'Fujifilm X-H2S', 2022, 2499.00),
    (5, 2, 'Panasonic Lumix S5', 2020, 1997.99),
    (5, 3, 'Panasonic Lumix S1H', 2019, 3997.99),
    (5, 2, 'Panasonic Lumix GH6', 2022, 2197.99),
]

DB2_LENSES = [
    (2, '70-200mm', 'f/2.8', 'Telephoto', 2799.95),
    (2, '14-24mm', 'f/2.8', 'Wide Angle', 1996.95),
    (2, '50mm', 'f/1.8', 'Prime', 226.95),
    (2, '24-120mm', 'f/4', 'Zoom', 1096.95),
    (4, '16-80mm', 'f/4', 'Zoom', 799.00),
    (4, '56mm', 'f/1.2', 'Portrait', 999.00),
    (4, '23mm', 'f/1.4', 'Prime', 899.00),
    (5, '24-105mm', 'f/4', 'Zoom', 1297.99),
    (5, '70-200mm', 'f/4', 'Telephoto', 1697.99),
    (5, '50mm', 'f/1.8', 'Prime', 247.99),
]

DB2_ACCESSORIES = [
    ('Nikon MB-D18 Grip', 'Battery Grip', 396.95, 'Nikon'),
    ('Nikon EN-EL15c Battery', 'Battery', 69.95, 'Nikon'),
    ('Nikon ME-1 Microphone', 'Microphone', 179.95, 'Nikon'),
    ('Nikon DK-32 Eyecup', 'Eyecup', 19.95, 'Nikon'),
    ('Fujifilm VG-XT4 Grip', 'Battery Grip', 349.00, 'Fujifilm'),
    ('Fujifilm NP-W235 Battery', 'Battery', 79.00, 'Fujifilm'),
    ('Fujifilm EF-X500 Flash', 'Flash', 449.00, 'Fujifilm'),
    ('Panasonic DMW-BGS5 Grip', 'Battery Grip', 347.99, 'Panasonic'),
    ('Panasonic DMW-BLK22 Battery', 'Battery', 97.99, 'Panasonic'),
    ('Rode VideoMic Pro', 'Microphone', 229.00, 'All Brands'),
]

# DB3 (Olympus, Leica, Pentax, Phase One) data
DB3_CAMERAS = [
    (6, 2, 'Olympus OM-1', 2022, 2199.99),
    (6, 2, 'Olympus OM-5', 2022, 1199.99),
    (6, 2, 'Olympus E-M1 Mark III', 2020, 1799.99),
    (7, 9, 'Leica Q3', 2023, 5995.00),
    (7, 9, 'Leica M11', 2022, 8995.00),
    (7, 2, 'Leica SL2-S', 2020, 4895.00),
    (8, 1, 'Pentax K-3 Mark III', 2021, 1999.95),
    (8, 4, 'Pentax 645Z', 2014, 6999.95),
    (10, 4, 'Phase One XF IQ4 150MP', 2019, 51990.00),
    (10, 4, 'Phase One XT', 2018, 44990.00),
]

DB3_LENSES = [
    (6, '12-40mm', 'f/2.8', 'Zoom', 999.00),
    (6, '40-150mm', 'f/2.8', 'Telephoto', 1499.00),
    (6, '25mm', 'f/1.2', 'Prime', 1199.00),
    (7, '50mm', 'f/2', 'Prime', 1895.00),
    (7, '35mm', 'f/1.4', 'Prime', 3795.00),
    (7, '90-280mm', 'f/2.8-4', 'Telephoto', 7995.00),
    (8, '55mm', 'f/1.4', 'Prime', 899.95),
    (8, '16-85mm', 'f/3.5-5.6', 'Zoom', 699.95),
    (10, '80mm', 'f/2.8', 'Prime', 3490.00),
    (10, '45mm', 'f/3.5', 'Wide Angle', 2990.00),
]

DB3_ACCESSORIES = [
    ('Olympus HLD-10 Grip', 'Battery Grip', 349.00, 'Olympus'),
    ('Olympus BLX-1 Battery', 'Battery', 89.99, 'Olympus'),
    ('Olympus FL-900R Flash', 'Flash', 579.00, 'Olympus'),
    ('Leica BP-SCL6 Battery', 'Battery', 195.00, 'Leica'),
    ('Leica Handgrip M', 'Hand Grip', 395.00, 'Leica'),
    ('Leica SF 64 Flash', 'Flash', 695.00, 'Leica'),
    ('Pentax D-BG8 Grip', 'Battery Grip', 299.95, 'Pentax'),
    ('Pentax D-LI90 Battery', 'Battery', 79.95, 'Pentax'),
    ('Phase One Battery', 'Battery', 295.00, 'Phase One'),
    ('Manfrotto MT055 Tripod', 'Tripod', 219.88, 'All Brands'),
]