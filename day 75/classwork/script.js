const child = document.getElementById("child");

        let left = 0;
        let topPos = 0;
        let direction = "down";

        const move = setInterval(function(){
            if(direction == "down"){
                topPos++;
                if(topPos == 450){
                    direction = "right";
                }
            } else if(direction == "right"){
                left++;
                if(left == 450){
                    direction = "up";
                }
            } else if(direction == "up"){
                topPos--;
                if(topPos == 0){
                    direction = "left";
                }
            } else {
                left--;
                if(left == 0){
                    direction = "down";
                }
            }

            child.style.left = left + 'px';
            child.style.top = topPos + 'px';
        }, 5);