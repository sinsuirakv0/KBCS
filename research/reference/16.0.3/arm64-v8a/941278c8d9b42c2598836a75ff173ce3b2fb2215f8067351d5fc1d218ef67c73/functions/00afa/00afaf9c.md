# 00afaf9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afaf9c",
  "name": "FUN_00afaf9c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26540d63ff6931715ee5d8e297cdecd4c5505bb070c441ddcf4d068d385798ef",
  "source_text_sha256": "26540d63ff6931715ee5d8e297cdecd4c5505bb070c441ddcf4d068d385798ef"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 639 bytes

~~~c

void FUN_00afaf9c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
                    /* try { // try from 00afafd4 to 00bfafdf has its CatchHandler @ 00afbae8 */
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afafe4 to 00bfaffb has its CatchHandler @ 00afbad0 */
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) = param_3 & 1;
  }
                    /* try { // try from 00afaffc to 00bfb057 has its CatchHandler @ 00afaee0 */
  return;
}

~~~
