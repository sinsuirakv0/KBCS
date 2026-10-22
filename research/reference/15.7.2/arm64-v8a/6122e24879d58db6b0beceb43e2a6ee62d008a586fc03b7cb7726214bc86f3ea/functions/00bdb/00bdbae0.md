# 00bdbae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbae0.md)

## 関数情報

~~~json
{
  "address": "00bdbae0",
  "name": "<EXTERNAL>::calloc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "50833963703739c867214cbbe98c0d29a26c5b20f1c7e21f4b8fc590fb14bab4",
  "source_text_sha256": "50833963703739c867214cbbe98c0d29a26c5b20f1c7e21f4b8fc590fb14bab4"
}
~~~
## 呼び出し元

- [0048cd38](../0048c/0048cd38.md)
- [0048df5c](../0048d/0048df5c.md)
- [00490630](../00490/00490630.md)
- [00495978](../00495/00495978.md)
- [004a1040](../004a1/004a1040.md)
- [004a1190](../004a1/004a1190.md)
- [004a1328](../004a1/004a1328.md)
- [004a15d0](../004a1/004a15d0.md)
- [004a5bdc](../004a5/004a5bdc.md)
- [004a6378](../004a6/004a6378.md)
- [004a6590](../004a6/004a6590.md)
- [004a6c9c](../004a6/004a6c9c.md)
- [004a710c](../004a7/004a710c.md)
- [004a728c](../004a7/004a728c.md)
- [004a7444](../004a7/004a7444.md)
- [004a76c0](../004a7/004a76c0.md)
- [004a8854](../004a8/004a8854.md)
- [004a8a10](../004a8/004a8a10.md)
- [004a8bc4](../004a8/004a8bc4.md)
- [004a8d78](../004a8/004a8d78.md)
- [004b76d8](../004b7/004b76d8.md)
- [004bf57c](../004bf/004bf57c.md)
- [004d989c](../004d9/004d989c.md)
- [005132d4](../00513/005132d4.md)
- [00513e2c](../00513/00513e2c.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [0051d4f0](../0051d/0051d4f0.md)
- [0051d614](../0051d/0051d614.md)
- [0051da48](../0051d/0051da48.md)
- [0051dbb0](../0051d/0051dbb0.md)
- [0051dca0](../0051d/0051dca0.md)
- [0051e054](../0051e/0051e054.md)
- [0051e2cc](../0051e/0051e2cc.md)
- [005204e8](../00520/005204e8.md)
- [00520804](../00520/00520804.md)
- [00520980](../00520/00520980.md)
- [00520afc](../00520/00520afc.md)
- [00521e04](../00521/00521e04.md)

## 呼び出し先

- [010a5118](../010a5/010a5118.md)

## 疑似コード 1/1 / UTF-8 230 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * calloc(size_t __nmemb,size_t __size)

{
  void *pvVar1;
  
  pvVar1 = (void *)(*(code *)PTR_calloc_00c1c5a8)();
  return pvVar1;
}

~~~
