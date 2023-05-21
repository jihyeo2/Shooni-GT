<template>
    <br/>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <section id="progress-bar" style="margin-top:-1%;">
        <div id="my-rounded-rectangle" class="my-rounded-rectangle"> 
        </div>
    </section>

    <section class="progress-icon" style="margin-top: 6%;">
        <div class="icon">
                <!-- <div style="position:relative; width:60%; margin-left: 20%;"> -->
                <div style="margin-right: 15%;">
                    <router-link to="/rent" class="no-underline">
                        <img src="../assets/images/school.png" alt="School" width="35" height="100">
                    </router-link>
                        <div style="text-align:bottom;font-weight:bold;font-family:avenir">School</div>
                </div>
                <div style="margin-right: 15%;">
                    <router-link to="/filter" class="no-underline">
                        <img src="../assets/images/price.png" alt="Price" width="20" height="100">
                    </router-link>
                    <div style="text-align:center;font-weight:bold;font-family:avenir">Price</div>
                </div>
                <div style="margin-right: 15%;">
                    <router-link to="/filter/1" class="no-underline">
                        <img src="../assets/images/prox.png" alt="Proximity" width="20">
                    </router-link>
                    <div style="text-align:center;font-weight:bold;font-family:avenir">Place</div>
                </div>
                <div style="margin-right: 15%;">
                    <router-link to="/filter/2" class="no-underline">
                        <img src="../assets/images/bed.png" alt="B&B" width="35" height="100">
                    </router-link>
                    <div style="text-align:center;font-weight:bold;font-family:avenir">Bed & Bath</div>
                </div>
                <div style="margin-right: 15%;">
                    <router-link to="/search" class="no-underline">
                        <img src="../assets/images/finish.png" alt="Finish" width="35" height="100">
                    </router-link>
                    <div style="text-align:center;font-weight:bold;font-family:avenir">Finish</div>
                </div>
                <!-- </div> -->
            </div> <!-- This is icon for progress bar close-->
        </section>

        <router-view></router-view>
</template>




<style>
.icon {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin-left: 13%;
}

.f1-my-rounded-rectangle {
    display: flex;
    background-color: #f1f1f1;
    border-radius: 10px;
    width: 1100px; /*  width */
    height: 20px; /*  height */
    margin: auto  ;
}
.btn-secondary {
  background-color: rgba(219, 116, 20, 0);
  color: #000000;
  border: solid white;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer; 
}
</style>