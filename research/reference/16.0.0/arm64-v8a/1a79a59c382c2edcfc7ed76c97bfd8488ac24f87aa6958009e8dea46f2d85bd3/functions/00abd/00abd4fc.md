# 00abd4fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abd4fc",
  "name": "FUN_00abd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115",
  "source_text_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115"
}
~~~

## 呼び出し元

- [0083f844](../0083f/0083f844.md)

## 呼び出し先

- [0046e784](../0046e/0046e784.md)
- [0046eeb8](../0046e/0046eeb8.md)
- [005c175c](../005c1/005c175c.md)

## 疑似コード / UTF-8 955 bytes

~~~c

void FUN_00abd4fc(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  param_1[0xb] = 0;
  puVar1 = param_1 + 10;
  *puVar1 = 0;
  param_1[9] = puVar1;
  param_1[1] = 0;
  *param_1 = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[8] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  FUN_0046eeb8(param_1 + 0x15);
  FUN_0046e784(param_1 + 0x2a);
                    /* try { // try from 00abd55c to 00bbd64f has its CatchHandler @ 00abd2c0 */
  *(undefined4 *)(param_1 + 0xd) = 0;
  param_1[0xc] = 0;
  param_1[7] = param_1[6];
  FUN_005c175c(param_1 + 9,param_1[10]);
  param_1[10] = 0;
  param_1[0xb] = 0;
  *(undefined4 *)(param_1 + 0xe) = 0xffffffff;
  param_1[9] = puVar1;
  *(undefined1 *)((long)param_1 + 0x6c) = 0;
  param_1[0x10] = param_1[0xf];
  param_1[0x13] = param_1[0x12];
  return;
}

~~~
