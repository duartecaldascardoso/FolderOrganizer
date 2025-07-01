import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ChakraProvider } from '@chakra-ui/react'
import { system } from "./theme.ts";
import ProductPageComponent from './components/ui/ProductPageComponent.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ChakraProvider value={system}>
      <ProductPageComponent/>
    </ChakraProvider>
  </StrictMode>,
)
