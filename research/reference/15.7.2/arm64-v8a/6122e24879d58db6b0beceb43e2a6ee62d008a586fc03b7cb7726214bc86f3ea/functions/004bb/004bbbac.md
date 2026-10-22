# 004bbbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004bbbac.md)

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "Botan::Power_Mod::window_bits",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06c0e994f160cf2ccf391d47b6d84ea7d7343090893d14a2b2d43946d0888341",
  "source_text_sha256": "06c0e994f160cf2ccf391d47b6d84ea7d7343090893d14a2b2d43946d0888341"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 904 bytes

~~~c

/* Botan::Power_Mod::window_bits(unsigned long, unsigned long, Botan::Power_Mod::Usage_Hints) */

long Botan::Power_Mod::window_bits(ulong param_1,undefined8 param_2,uint param_3)

{
  long lVar1;
  undefined *puVar2;
  
  if (param_1 == 0) {
LAB_004bbbd8:
    lVar1 = 1;
  }
  else {
    if (param_1 < 0x59a) {
      if (param_1 < 0x21b) {
        if (param_1 < 0xc5) {
          if (param_1 < 0x46) {
            if (param_1 < 0x19) goto LAB_004bbbd8;
            puVar2 = &UNK_002b99b8;
          }
          else {
            puVar2 = &UNK_002b99a8;
          }
        }
        else {
          puVar2 = &UNK_002b9998;
        }
      }
      else {
        puVar2 = &UNK_002b9988;
      }
    }
    else {
      puVar2 = &UNK_002b9978;
    }
    lVar1 = *(long *)(puVar2 + 8) + 1;
  }
  return lVar1 + (ulong)((param_3 & 1) << 1 | param_3 >> 10 & 1);
}

~~~
