import styled from "styled-components";

const Header = (props) => {
  return <Nav>Navbar</Nav>;
};

const Nav = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 70px;
  display: flex;
  background-color: #597E52;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  letter-spacing: 16px;
  z-index: 3;
`;

export default Header;