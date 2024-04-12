import styled from "styled-components";

const Login = () => {
  return (
    <login>
      <UserLogin>
        userlogin
      </UserLogin>
      <Collectorlogin>collectorlogin</Collectorlogin>
    </login>
  );
};

export default Login;

const login = styled.div`
  overflow: hidden;
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  text-align: center;
  height: 100vh;
`;

const UserLogin = styled.div`

`;

const Collectorlogin = styled.div`
  
`;
