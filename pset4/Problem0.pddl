;; There is only one block, A, which is on the table.  A sprayer with
;; red paint is on the table.  Our goal is to have A be red and the
;; arm empty.

(define (problem 0)
  (:domain hw7)
  (:objects A S1 Red)
  (:init (arm-empty)
	 (Block A)  (on-table A) (Color Red)
 	 (Sprayer S1) (on-table S1) (is-color Red S1)
         )
  (:goal (and (arm-empty)
              (is-color Red A)
          )))
