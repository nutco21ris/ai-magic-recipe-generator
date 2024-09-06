import React, { ReactNode } from 'react'
import { AppBar, Toolbar, Typography, Container, Box } from '@mui/material'
import { styled } from '@mui/system'

interface LayoutProps {
  children: ReactNode
}

const StyledMain = styled('main')(({ theme }) => ({
  backgroundColor: theme.palette.background.default,
  minHeight: '100vh',
  paddingTop: theme.spacing(8),
  paddingBottom: theme.spacing(8),
}))

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Harry Potter Magic Recipe Generator</Typography>
        </Toolbar>
      </AppBar>
      <StyledMain>
        <Container maxWidth="lg">
          {children}
        </Container>
      </StyledMain>
      <Box component="footer" sx={{ bgcolor: 'background.paper', py: 6 }}>
        <Container maxWidth="lg">
          <Typography variant="body2" color="text.secondary" align="center">
            © {new Date().getFullYear()} Harry Potter Magic Recipe Generator
          </Typography>
        </Container>
      </Box>
    </>
  )
}

export default Layout