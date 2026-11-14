# 006bedac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "006bedac",
  "name": "FUN_006bedac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fbe62027b3bc584fc48eacaeb8d3eab9fa7c8c2ee5ffddf8217885e551cd14ee",
  "source_text_sha256": "fbe62027b3bc584fc48eacaeb8d3eab9fa7c8c2ee5ffddf8217885e551cd14ee"
}
~~~

## 呼び出し元

- [006bc0a0](../006bc/006bc0a0.md)
- [00720498](../00720/00720498.md)
- [0076a1b8](../0076a/0076a1b8.md)
- [007bea00](../007be/007bea00.md)
- [007cdea8](../007cd/007cdea8.md)
- [007e00a4](../007e0/007e00a4.md)
- [008080c0](../00808/008080c0.md)
- [0089e4cc](../0089e/0089e4cc.md)
- [009258c8](../00925/009258c8.md)
- [00986418](../00986/00986418.md)
- [0098df8c](../0098d/0098df8c.md)
- [0098ec08](../0098e/0098ec08.md)
- [0099803c](../00998/0099803c.md)
- [00a8f618](../00a8f/00a8f618.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 361 bytes

~~~c

uint FUN_006bedac(long param_1,long param_2)

{
  byte *pbVar1;
  
  pbVar1 = (byte *)(param_1 + param_2 * 4);
  return (uint)(*(byte *)(param_1 + 0x2a) ^ pbVar1[2]) << 0x10 |
         (uint)(*(byte *)(param_1 + 0x2b) ^ pbVar1[3]) << 0x18 |
         (uint)(*(byte *)(param_1 + 0x29) ^ pbVar1[1]) << 8 |
         (uint)(*(byte *)(param_1 + 0x28) ^ *pbVar1);
}

~~~
