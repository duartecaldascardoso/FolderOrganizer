'use client'

import {
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Flex,
} from '@chakra-ui/react'

export default function ProductPageComponent() {
  return (
    <Flex
      minH="100vh"
      align="center"
      justify="center"
      bg="white"
      px={4}
    >
      <Container maxW="3xl" py={{ base: 20, md: 36 }}>
        <Stack textAlign="center" gap={{ base: 8, md: 14 }}>
          <Heading
            as="h1"
            fontWeight="bold"
            fontSize={{ base: '3xl', sm: '5xl', md: '6xl' }}
            lineHeight="110%">
            Organize your folders <br />
            <Text as="span" color="purple.400" textDecorationLine={'underline'}>
              with intelligence
            </Text>
          </Heading>

          <Text fontSize="lg">
            SmartSort uses AI to automatically organize your workspace,
            making it adapt to your intentions and daily usage. 
          </Text>

          <Stack
            direction={{sm: 'row' }}
            gap={4}
            justify="center"
            align="center"
            position="relative">
            <Button
              colorScheme="green"
              rounded="full"
              px={8}
              size="lg"
              _hover={{ bg: 'purple.500' }}>
              Get Started
            </Button>
          </Stack>
        </Stack>
      </Container>
    </Flex>
  )
}
