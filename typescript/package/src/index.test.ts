import { expect, it } from 'vitest'

import { fn } from '../src/index.ts'

it('must return greeting message', () => {
  expect(fn()).toBe('Hello, world!')
})
