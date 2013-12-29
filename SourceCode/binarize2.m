%%binarizes the image using Otsu and remove the lines detectd by the 
%%funcion blacklines
%%Jul 17 Luiz

function [binary_image] = binarize2( I )

  
    level = graythresh(I);

    bw = im2bw(I, level);
    
    %imshow(bw) ;    
    %waitforbuttonpress

    [h,w] = size(bw);

    for i = 1:h
        vet(i) =  sum(bw(i,:)) ;
    end
    
    [ number_of_black_lines, pos ] = blacklines( vet, w ) ;
    
    % remove black lines
   
    for i=1:number_of_black_lines
        bw(pos(i),:) = 1 ;
        fprintf('Removing line %d\n', pos(i)) ;
    end
    
    %median filter to remove the salt and pepper noise
    %imshow(bw) ;
    %waitforbuttonpress

    bw = medfilt2(bw) ;
    
    % white borders
    [h,w] = size(bw);
    bw(1,:) = 1 ;
    bw(h,:) = 1 ;
    bw(:,1) = 1 ;
    bw(:,w) = 1 ;

    %imshow(bw) ;
    
    
    
    binary_image = bw ;
    

end



