# 00aa3bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aa3bec.md)

## 関数情報

~~~json
{
  "address": "00aa3bec",
  "name": "FUN_00aa3bec",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfe4865d13dca49ea71cc25ee4a6126c3107a92d75eb478aa406d874352242f9",
  "source_text_sha256": "dfe4865d13dca49ea71cc25ee4a6126c3107a92d75eb478aa406d874352242f9"
}
~~~
## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [0069ef54](../0069e/0069ef54.md)
- [009f1e64](../009f1/009f1e64.md)
- [00a960ac](../00a96/00a960ac.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa4fb0](../00aa4/00aa4fb0.md)

## 疑似コード 1/1 / UTF-8 1173 bytes

~~~c

ulong FUN_00aa3bec(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa3c04 to 00ba3c13 has its CatchHandler @ 00aa599c */
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa3c14 to 00ba3c27 has its CatchHandler @ 00aa5974 */
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
                    /* try { // try from 00aa3c28 to 00ba3c5f has its CatchHandler @ 00aa3a30 */
  lVar2 = FUN_0081f580();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0xa4e4) != 0)
    ;
  }
  else {
                    /* try { // try from 00aa3c74 to 00ba3c87 has its CatchHandler @ 00aa59e0 */
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f008);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00aa4fb0(0,param_2,param_3,0x800);
      return uVar3;
    }
  }
                    /* try { // try from 00aa3c60 to 00ba3c73 has its CatchHandler @ 00aa59e4 */
  return uVar3;
}

~~~
