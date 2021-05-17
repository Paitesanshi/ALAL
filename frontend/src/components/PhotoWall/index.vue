<template>
  <div class="grid" id="grid">
    <photo-card
      img="https://i.picsum.photos/id/1016/3844/2563.jpg?hmac=WEryKFRvTdeae2aUrY-DHscSmZuyYI9jd_-p94stBvc"
      link="#"
    ></photo-card>
    <photo-card
      img="https://i.picsum.photos/id/1018/3914/2935.jpg?hmac=3N43cQcvTE8NItexePvXvYBrAoGbRssNMpuvuWlwMKg"
      link="#"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/1012/3973/2639.jpg?hmac=s2eybz51lnKy2ZHkE2wsgc6S81fVD1W2NKYOSh8bzDc"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/1013/4256/2832.jpg?hmac=UmYgZfqY_sNtHdug0Gd73bHFyf1VvzFWzPXSr5VTnDA"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/101/2621/1747.jpg?hmac=cu15YGotS0gIYdBbR1he5NtBLZAAY6aIY5AbORRAngs"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/1023/3955/2094.jpg?hmac=AW_7mARdoPWuI7sr6SG8t-2fScyyewuNscwMWtQRawU"
    ></photo-card>
    <photo-card
      link=""
      img="https://i.picsum.photos/id/1024/1920/1280.jpg?hmac=-PIpG7j_fRwN8Qtfnsc3M8-kC3yb0XYOBfVzlPSuVII"
    ></photo-card>
    <photo-card
      img="https://i.picsum.photos/id/1016/3844/2563.jpg?hmac=WEryKFRvTdeae2aUrY-DHscSmZuyYI9jd_-p94stBvc"
      link="#"
    ></photo-card>
  </div>
</template>
<script>
export default {
  name: "PhotoWall",
  data() {},
  computed() {},
  created() {
    Vue.component("photo-card", {
      template: `<a class="card"
                :href="link"
                target="_blank"
                ref="card"
                @mousemove="move"
                @mouseleave="leave"
                @mouseover="over">
                  <div class="reflection" ref="refl"></div>
                  <img :src="img"/>
            </a>`,
      props: ["img", "link"],
      mounted() {},
      data: () => ({
        debounce: null
      }),

      methods: {
        over() {
          const refl = this.$refs.refl;
          refl.style.opacity = 1;
        },
        leave() {
          const card = this.$refs.card;
          const refl = this.$refs.refl;
          card.style.transform = `perspective(500px) scale(1)`;
          refl.style.opacity = 0;
        },

        move() {
          const card = this.$refs.card;
          const refl = this.$refs.refl;

          const relX = (event.offsetX + 1) / card.offsetWidth;
          const relY = (event.offsetY + 1) / card.offsetHeight;
          const rotY = `rotateY(${(relX - 0.5) * 60}deg)`;
          const rotX = `rotateX(${(relY - 0.5) * -60}deg)`;
          card.style.transform = `perspective(500px) scale(2) ${rotY} ${rotX}`;

          const lightX = this.scale(relX, 0, 1, 150, -50);
          const lightY = this.scale(relY, 0, 1, 30, -100);
          const lightConstrain = Math.min(Math.max(relY, 0.3), 0.7);
          const lightOpacity = this.scale(lightConstrain, 0.3, 1, 1, 0) * 255;
          const lightShade = `rgba(${lightOpacity}, ${lightOpacity}, ${lightOpacity}, 1)`;
          const lightShadeBlack = `rgba(0, 0, 0, 1)`;
          refl.style.backgroundImage = `radial-gradient(circle at ${lightX}% ${lightY}%, ${lightShade} 20%, ${lightShadeBlack})`;
        },
        scale: (val, inMin, inMax, outMin, outMax) =>
          outMin + ((val - inMin) * (outMax - outMin)) / (inMax - inMin)
      }
    });
  },
  methods: {}
};
</script>
<style>
body {
  margin: 0;
  min-height: 100vh;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  flex-direction: column;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  background-image: radial-gradient(circle, #fff 30%,pink);
  padding: 0 40px;
  font-family: "Source Sans Pro", Helvetica, sans-serif;
  font-weight: 300;
}

#grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, 150px);
  grid-column-gap: 30px;
  grid-row-gap: 30px;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  width: 100%;
  max-width: 700px;
}
#grid .card {
  background-color: #ccc;
  width: 150px;
  height: 150px;
  -webkit-transition: all 0.1s ease;
  transition: all 0.1s ease;
  border-radius: 3px;
  position: relative;
  z-index: 1;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0);
  overflow: hidden;
  cursor: pointer;
}
#grid .card:hover {
  -webkit-transform: scale(2);
  transform: scale(2);
  z-index: 2;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
}
#grid .card:hover img {
  -webkit-filter: grayscale(0);
  filter: grayscale(0);
}
#grid .card .reflection {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 2;
  left: 0;
  top: 0;
  -webkit-transition: all 0.1s ease;
  transition: all 0.1s ease;
  opacity: 0;
  mix-blend-mode: soft-light;
}
#grid .card img {
  width: 100%;
  height: 100%;
  -o-object-fit: cover;
  object-fit: cover;
  -webkit-filter: grayscale(0.65);
  filter: grayscale(0.65);
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
</style>
