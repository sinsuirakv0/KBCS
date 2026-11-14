# 00afad6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afad6c",
  "name": "FUN_00afad6c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd43ba77f81938c2e0d33c1f2bf8c84d80dbf84d591333a0761fc11a44077f01",
  "source_text_sha256": "bd43ba77f81938c2e0d33c1f2bf8c84d80dbf84d591333a0761fc11a44077f01"
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 579 bytes

~~~c

bool FUN_00afad6c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008524fc();
                    /* try { // try from 00afadac to 00bfadaf has its CatchHandler @ 00afaeb8 */
                    /* try { // try from 00afadb0 to 00bfae3f has its CatchHandler @ 00afad10 */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a80) != 0;
  }
  return bVar1;
}

~~~
