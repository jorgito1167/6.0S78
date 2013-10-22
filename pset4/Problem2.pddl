
;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored ref and B
;; blue and the brush be clean. 

(define (problem 2)
  (:domain hw7)
  (:objects A B bucket1 brush1 sprayer1 can1 Red Blue Yellow Green )
  (:init (arm-empty)
    (Block A) (on-table A) 
    (Block B) (on B A) (clear B)
    (Sprayer sprayer1) (on-table sprayer1) (clear sprayer1) (has-color Blue sprayer1)
    (Can can1) (has-color Red can1) (clear can1)
    (Brush brush1) (clear brush1) (clean brush1) (on-table brush1)
    (Bucket bucket1) (clear bucket1)
    (Color Red) (Color Blue) (Color Green) (Color Yellow)
      )
  (:goal (and (arm-empty)
              (is-color Red A)
              (is-color Blue B)
              (clean brush1)
           )))
