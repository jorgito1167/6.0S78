
;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored ref and B
;; blue and the brush be clean. 

(define (problem 2)
  (:domain hws6)
  (:objects A B bucket1 brush1 sprayer1 can1 Red Blue Yellow Green )
  (:init (arm-empty)
    (Block A) (on-table A) 
         ... block A is on the table ...
    (Block B) (on B A) (clear B)
   ... block B is on block A and there's nothing on B ...
    (Sprayer sprayer1) (on-table sprayer1) (clear sprayer1)
         ... there is a blue sprayer on the table and nothing is on it ...
    (Can can1) (is-color Red can1) (clear can1)
   ... there is a red paint can on the table and noting is on it ...
    (Brush brush1) (clear brush1) (clean brush1)
   ... there is a clean brush on the table and nothing is on it  ...
    (Bucket bucket1) (clear bucket1)
   ... there is a water bucket on the table and nothing is on it ...
    (Color Red) (Color Blue) (Color Green) (Color Yellow)
      )
  (:goal (and (arm-empty)
              (is-color Red A)
              ... A is red ...
              (is-color Blue B)
              ... B is blue ...
              (clean brush1)
              ... the brush is clean ...
           )))
