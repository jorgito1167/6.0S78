(define (problem 0)
  (:domain hw7)
  (:objects A can1 brush1 Red Green Yellow Blue)
  (:init (arm-empty)
	 (Block A)  (on-table A) (clear A) (Color Red) (Color Green) (Color Yellow) (Color Blue) 
 	 (Can can1) (has-color Red can1) (clear can1)
   (Brush brush1) (Clean brush1) (on-table brush1) (clear brush1)
         )
  (:goal (and (arm-empty)
              (is-color Red A)
          )))
