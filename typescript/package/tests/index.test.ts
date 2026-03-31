import { expect, it, vi } from 'vitest'

import { fn } from '../src/index.ts'

it('must log greeting message to the console', () => {
  using consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => void {})

  const result = fn()
  console.log(result)

  expect(result).toBeDefined()
  expect(consoleSpy).toHaveBeenCalledWith(result)
})
