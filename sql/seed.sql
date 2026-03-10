INSERT INTO species 
(name, scientific_name, family, conservation_status, wingspan_cm)
VALUES
('House Sparrow','Passer domesticus','Passeridae','Least Concern',21.0),
('European Robin','Erithacus rubecula','Muscicapidae','Least Concern',22.5),
('Barn Owl','Tyto alba','Tytonidae','Least Concern',95.0),
('White Stork','Ciconia ciconia','Ciconiidae','Least Concern',195.0);

INSERT INTO birds (nickname, ring_code, age, species_id)
VALUES
('Jack', 'HS-001', 2, 1),
('Ruby', 'ER-001', 1, 2),
('Ghost', 'BO-001', 4, 3),
('Cloud', 'WS-001', 3, 4);

INSERT INTO birdspotting (bird_id, spotted_at, location, observer_name, notes)
VALUES
  (1, '2026-03-01 08:15:00', 'Brussels Park', 'Nina Peeters', 'Seen near the fountain'),
  (1, '2026-03-02 09:40:00', 'Ghent Riverside', 'Lars Mertens', 'Feeding on breadcrumbs'),
  (2, '2026-03-02 07:55:00', 'Antwerp Zoo Garden', 'Emma Janssens', 'Singing from a low branch'),
  (3, '2026-03-03 21:10:00', 'Ardennes Forest Edge', 'Tom Wouters', 'Hunting at dusk'),
  (4, '2026-03-04 12:25:00', 'Leuven Wetlands', 'Sofie Claes', 'Resting close to the marsh');