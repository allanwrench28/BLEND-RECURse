import React from 'react';
import { ThemeProvider } from 'styled-components';
import GlobalStyle from './themes/GlobalStyle';
import darkTheme from './themes/darkTheme';
import Dashboard from './components/Dashboard';

const App: React.FC = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <GlobalStyle />
      <Dashboard />
    </ThemeProvider>
  );
};

export default App;
