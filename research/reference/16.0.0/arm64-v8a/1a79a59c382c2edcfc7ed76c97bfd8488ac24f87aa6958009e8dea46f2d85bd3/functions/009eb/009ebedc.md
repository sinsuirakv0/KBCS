# 009ebedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009ebedc",
  "name": "FUN_009ebedc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "500354848f4eb5220cf1801b8e18c6aa51ce1131b666325a5b54829a62efcf2d",
  "source_text_sha256": "500354848f4eb5220cf1801b8e18c6aa51ce1131b666325a5b54829a62efcf2d"
}
~~~

## 呼び出し元

- [009eade8](../009ea/009eade8.md)

## 呼び出し先

- [009f2cc8](../009f2/009f2cc8.md)

## 疑似コード / UTF-8 666 bytes

~~~c

void FUN_009ebedc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  
                    /* try { // try from 009ebedc to 00aebeeb has its CatchHandler @ 009ebf90 */
                    /* try { // try from 009ebeec to 00aec02f has its CatchHandler @ 009ebe14 */
  puVar1 = *(undefined8 **)(param_1 + 8);
  if (puVar1 < *(undefined8 **)(param_1 + 0x10)) {
    uVar3 = *param_2;
    puVar2 = puVar1 + 2;
    puVar1[1] = param_2[1];
    *puVar1 = uVar3;
    *param_2 = 0;
    param_2[1] = 0;
  }
  else {
    puVar2 = (undefined8 *)FUN_009f2cc8(param_1);
  }
  *(undefined8 **)(param_1 + 8) = puVar2;
  return;
}

~~~
