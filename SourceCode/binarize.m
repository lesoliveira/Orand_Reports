function [binary_image] = binarize( I )

  
    level = graythresh(I);

    bw = im2bw(I, level);
    
    %imshow(bw) ;    
    %waitforbuttonpress

    [h,w] = size(bw);

    for i = 1:h
        vet(i) =  sum(bw(i,:)) ;
    end

    [valMin, indexMin ] = min(vet) ;
    
    %display(valMin/w)

    %if the line is the first
    if( indexMin == 1)
        bw(1,:) = 1 ;
        indexMin = 2 ;
    end
    
    %if the line is the last
    if( indexMin == h)
        bw(h+1,:) = 1 ;
    end

    %%If the line is big enough
    if(valMin/w < .20 )

        %%create a subimage
        imgLine(1,:) = bw(indexMin-1,:) ;
        imgLine(2,:) = bw(indexMin,:) ;
        imgLine(3,:) = bw(indexMin+1,:) ;
        
        %imshow(imgLine) ;
        %waitforbuttonpress      

        %%dilate this subimage use el (structuring element)

        el = strel('line',3, 45) ;

        imgDil = imdilate(imgLine,el) ;

        %%put back this subimage into the original image
        bw(indexMin-1,:) = imgDil(1,:);
        bw(indexMin,:) = imgDil(2,:) ;
        bw(indexMin+1,:) =imgDil(3,:) ;

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

