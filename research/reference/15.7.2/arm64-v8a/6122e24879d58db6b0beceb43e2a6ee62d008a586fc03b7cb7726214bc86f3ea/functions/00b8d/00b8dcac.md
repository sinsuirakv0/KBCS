# 00b8dcac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b8dcac.md)

## 関数情報

~~~json
{
  "address": "00b8dcac",
  "name": "FUN_00b8dcac",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e4b79d1eb3506db8a99b65093e15afbff703a613461ab0e1ba27b92ccd31084",
  "source_text_sha256": "5e4b79d1eb3506db8a99b65093e15afbff703a613461ab0e1ba27b92ccd31084"
}
~~~
## 呼び出し元

- [00b8d5b8](../00b8d/00b8d5b8.md)
- [00b90a2c](../00b90/00b90a2c.md)

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1490](../00be1/00be1490.md)

## 疑似コード 1/1 / UTF-8 1006 bytes

~~~c

int FUN_00b8dcac(char *param_1,__locale_t param_2,char *param_3,undefined8 param_4,
                undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  int iVar1;
  __locale_t __dataset;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  __dataset = uselocale(param_2);
                    /* catch() { ... } // from try @ 00b8dc98 with catch @ 00b8dd24 */
  uStack_58 = 0xffffff80ffffffd8;
  local_70 = (undefined1 *)register0x00000008;
  ppuStack_68 = &local_70;
  puStack_60 = auStack_a0;
  iVar1 = vsscanf(param_1,param_3,&local_70);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  return iVar1;
}

~~~
