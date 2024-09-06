import type { AppProps } from 'next/app'
import { useState } from 'react'
import { QueryClient, QueryClientProvider } from 'react-query'
import { ThemeProvider } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'
import theme from '../styles/theme'
import '../styles/globals.css'

// Add the following line to enable JSX
/** @jsxImportSource @emotion/react */

function MyApp({ Component, pageProps }: AppProps) {
    const [queryClient] = useState(() => new QueryClient())
  
    return (
      <QueryClientProvider client={queryClient}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <Layout>
            <Component {...pageProps} />
          </Layout>
        </ThemeProvider>
      </QueryClientProvider>
    )
  }

export default MyApp