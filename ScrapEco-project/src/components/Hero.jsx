import styled from "styled-components";

const Login = (props) => {
  return (
    <Container>
      <Content>
        <Hero>
          <Heading>
            Closing the Loop: The Sustainable E-waste Recycling Process,
          </Heading>
          <Description>
            ScrapEco revolutionizes e-waste management in India, using AI and
            intuitive interfaces. Users upload e-waste photos for accurate
            pricing estimates, facilitating kabadi walas' bidding for items.
            Revenue from recycling is fairly distributed, incentivizing
            participation and promoting sustainability. ScrapEco's holistic
            approach redirects e-waste from landfills, conserves resources, and
            fosters a circular economy for a better future.
          </Description>
          <HeroImg src="/images/Hero.jpeg" />
        </Hero>
        <login>
          <UserLogin>user login</UserLogin>
          <Collectorlogin>collector login</Collectorlogin>
        </login>
      </Content>
    </Container>
  );
};

const Container = styled.section`
  overflow: hidden;
  display: flex;
  flex-direction: column;
  text-align: center;
  height: 100vh;
`;

const Content = styled.div`
  margin-bottom: 100vw;
  width: 100%;
  position: relative;
  min-height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 80px 40px;
  height: 100%;
`;

const Hero = styled.div`
  margin-bottom: 2vw;
  max-width: 650px;
  flex-wrap: wrap;
  display: flex;
  flex-directrion: column;
  justify-content: space-between;
  margin-top: 150px;
  align-items: center;
  text-align: center;
  margin-right: auto;
  margin-left: auto;
  transition-timing-function: ease-out;
  transition: opacity 0.2s;
  width: 100%;
`;

const Description = styled.p`
  color: black;
  font-size: 20px;
  margin: 0 0 24px;
  line-height: 1.5;
  letter-spacing: 1.5;
`;

const Heading = styled.h1`
  color: black;
  font-size: 38px;
  marin: 0 0 6px;
  line-height: 1.5;
  letter-spacing: 1.5;
`;

const HeroImg = styled.img`
  margin: auto;
  display: inline-block;
  verticle-align: bottom;
  margin-top: 5px;
`;

const login = styled.div`
  display: flex;
  justify-content: space-around;
`;
const UserLogin = styled.div``;

const Collectorlogin = styled.div``;

export default Login;
