# 00b8daec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b8daec.md)

## 関数情報

~~~json
{
  "address": "00b8daec",
  "name": "std::__ndk1::__num_get<char>::__stage2_int_loop",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b86e347fdef824e317d4cbfdc875c0b21aed14f0e1f348e0c57afd82d3f80ea",
  "source_text_sha256": "1b86e347fdef824e317d4cbfdc875c0b21aed14f0e1f348e0c57afd82d3f80ea"
}
~~~
## 呼び出し元

- [00be1430](../00be1/00be1430.md)

## 呼び出し先

- [00bdb080](../00bdb/00bdb080.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~
## 疑似コード 1/1 / UTF-8 2867 bytes

~~~c

/* std::__ndk1::__num_get<char>::__stage2_int_loop(char, int, char*, char*&, unsigned int&, char,
   std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >
   const&, unsigned int*, unsigned int*&, char*) */

undefined8
std::__ndk1::__num_get<char>::__stage2_int_loop
          (char param_1,int param_2,char *param_3,char **param_4,uint *param_5,char param_6,
          basic_string *param_7,uint *param_8,uint **param_9,char *param_10)

{
  ulong uVar1;
  char *pcVar2;
  undefined *puVar3;
  char *pcVar4;
  undefined8 uVar5;
  char cVar6;
  long lVar7;
  uint *puVar8;
  char *pcVar9;
  
  pcVar9 = *param_4;
  if (pcVar9 == param_3) {
    if (param_10[0x18] == param_1) {
      cVar6 = '+';
LAB_00b8dbd0:
      *param_4 = param_3 + 1;
      *param_3 = cVar6;
      *param_5 = 0;
      return 0;
    }
    if (param_10[0x19] == param_1) {
      cVar6 = '-';
      goto LAB_00b8dbd0;
    }
  }
  uVar1 = (ulong)((byte)*param_7 >> 1);
  if (((byte)*param_7 & 1) != 0) {
    uVar1 = *(ulong *)(param_7 + 8);
  }
  if ((param_1 == param_6) && (uVar1 != 0)) {
    puVar8 = *param_9;
                    /* try { // try from 00b8db4c to 00c8dc97 has its CatchHandler @ 00b8db4c
                       catch() { ... } // from try @ 00b8db4c with catch @ 00b8db4c
                       catch() { ... } // from try @ 00b8dca4 with catch @ 00b8db4c */
    if ((long)puVar8 - (long)param_8 < 0xa0) {
      *puVar8 = *param_5;
      *param_9 = puVar8 + 1;
      *param_5 = 0;
      return 0;
    }
    return 0;
  }
  pcVar4 = memchr(param_10,(uint)(byte)param_1,0x1a);
  puVar3 = PTR___src_00c1bc90;
  pcVar2 = param_10 + 0x1a;
  if (pcVar4 != (char *)0x0) {
    pcVar2 = pcVar4;
  }
  lVar7 = (long)pcVar2 - (long)param_10;
  if (lVar7 < 0x18) {
    if (param_2 == 8) {
LAB_00b8dc08:
      if ((long)(ulong)(uint)param_2 <= lVar7) goto LAB_00b8dbb8;
    }
    else if (param_2 == 0x10) {
      if (0x15 < lVar7) {
        if (pcVar9 == param_3) {
          return 0xffffffff;
        }
        if (2 < (long)pcVar9 - (long)param_3) {
          return 0xffffffff;
        }
        if (pcVar9[-1] != '0') {
          return 0xffffffff;
        }
        *param_5 = 0;
                    /* try { // try from 00b8dc98 to 00c8dca3 has its CatchHandler @ 00b8dd24 */
        cVar6 = puVar3[lVar7];
        *param_4 = pcVar9 + 1;
                    /* try { // try from 00b8dca4 to 00c8dd4b has its CatchHandler @ 00b8db4c */
        *pcVar9 = cVar6;
        return 0;
      }
    }
    else if (param_2 == 10) goto LAB_00b8dc08;
    uVar5 = 0;
    cVar6 = PTR___src_00c1bc90[lVar7];
    *param_4 = pcVar9 + 1;
    *pcVar9 = cVar6;
    *param_5 = *param_5 + 1;
  }
  else {
LAB_00b8dbb8:
    uVar5 = 0xffffffff;
  }
  return uVar5;
}

~~~
