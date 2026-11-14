# 00afd6ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afd6ec",
  "name": "FUN_00afd6ec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00eb8dd54df6217aed0d3f97e39cba997f053a3524182b49752b9a9716c33132",
  "source_text_sha256": "00eb8dd54df6217aed0d3f97e39cba997f053a3524182b49752b9a9716c33132"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [005f3e60](../005f3/005f3e60.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [007082e8](../00708/007082e8.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00afd6ec(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afd6f8 to 00bfd70f has its CatchHandler @ 00afd9f0 */
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afd71c to 00bfd743 has its CatchHandler @ 00afdbb4 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b64);
}

~~~
