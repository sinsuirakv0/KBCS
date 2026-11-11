# 009dcecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70",
  "source_text_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70"
}
~~~

## 呼び出し元

- [0063acb4](../0063a/0063acb4.md)
- [0063b54c](../0063b/0063b54c.md)
- [0063bc98](../0063b/0063bc98.md)
- [0064ecb8](../0064e/0064ecb8.md)
- [006c0f38](../006c0/006c0f38.md)
- [006c119c](../006c1/006c119c.md)
- [006c2018](../006c2/006c2018.md)
- [006d3e3c](../006d3/006d3e3c.md)
- [006dd264](../006dd/006dd264.md)
- [006de788](../006de/006de788.md)
- [006dea94](../006de/006dea94.md)
- [006e1ea8](../006e1/006e1ea8.md)
- [006e3320](../006e3/006e3320.md)
- [006f24d4](../006f2/006f24d4.md)
- [00769d84](../00769/00769d84.md)
- [008dc120](../008dc/008dc120.md)
- [008e66ac](../008e6/008e66ac.md)
- [008ef9f4](../008ef/008ef9f4.md)
- [008f3044](../008f3/008f3044.md)
- [0098dc08](../0098d/0098dc08.md)
- [00a75dac](../00a75/00a75dac.md)

## 呼び出し先

- [0085b2a4](../0085b/0085b2a4.md)
- [0085b2ac](../0085b/0085b2ac.md)
- [0085b2b4](../0085b/0085b2b4.md)
- [0085b2bc](../0085b/0085b2bc.md)

## 疑似コード / UTF-8 1529 bytes

~~~c

undefined8 FUN_009dcecc(undefined8 param_1,int param_2,int param_3,int param_4,int param_5)

{
  int iVar1;
  
                    /* try { // try from 009dcee8 to 00adceef has its CatchHandler @ 009dcfd4 */
  iVar1 = FUN_0085b2a4();
  if (param_2 <= iVar1) {
                    /* try { // try from 009dcf04 to 00adcf23 has its CatchHandler @ 009dcfec */
    iVar1 = FUN_0085b2a4(param_1);
    if ((iVar1 <= param_4 + param_2) && (iVar1 = FUN_0085b2ac(param_1), param_3 <= iVar1)) {
      iVar1 = FUN_0085b2ac(param_1);
                    /* try { // try from 009dcf38 to 00adcf3f has its CatchHandler @ 009dcfb0 */
                    /* try { // try from 009dcf54 to 00adcf5b has its CatchHandler @ 009dcf60 */
                    /* catch() { ... } // from try @ 009dcc3c with catch @ 009dcf5c
                       try { // try from 009dcf5c to 00add02f has its CatchHandler @ 009dc934 */
                    /* catch() { ... } // from try @ 009dcc08 with catch @ 009dcf60
                       catch() { ... } // from try @ 009dcf54 with catch @ 009dcf60 */
      if (((iVar1 <= param_5 + param_3) &&
          (((iVar1 = FUN_0085b2b4(param_1), param_2 <= iVar1 &&
            (iVar1 = FUN_0085b2b4(param_1), iVar1 <= param_4 + param_2)) &&
           (iVar1 = FUN_0085b2bc(param_1), param_3 <= iVar1)))) &&
         (iVar1 = FUN_0085b2bc(param_1), iVar1 <= param_5 + param_3)) {
        return 1;
      }
    }
  }
                    /* catch() { ... } // from try @ 009dce44 with catch @ 009dcf78 */
  return 0;
}

~~~
