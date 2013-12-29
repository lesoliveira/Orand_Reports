function [ number_of_black_lines, pos ] = blacklines( vet, w )

    pos = [] ;
    number_of_black_lines = 0 ;
    
    [p1, sv] = size(vet) ;
    
    for i = 1:sv
        if(vet(i)/w < 0.2)
            number_of_black_lines = number_of_black_lines + 1;
            pos(number_of_black_lines) = i;
            
    end
    

end

