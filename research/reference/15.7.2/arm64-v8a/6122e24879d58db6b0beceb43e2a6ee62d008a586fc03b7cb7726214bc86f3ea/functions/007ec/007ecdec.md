# 007ecdec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007ecdec.md)

## 関数情報

~~~json
{
  "address": "007ecdec",
  "name": "FUN_007ecdec",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b7cfd85e09eec818b9e367e635f5d143689c38adeab2c089ff1a5f9c73dc8582",
  "source_text_sha256": "b7cfd85e09eec818b9e367e635f5d143689c38adeab2c089ff1a5f9c73dc8582"
}
~~~
## 呼び出し元

- [0099a654](../0099a/0099a654.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [007eca30](../007ec/007eca30.md)
- [007ecd04](../007ec/007ecd04.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~
## 疑似コード 1/1 / UTF-8 2073 bytes

~~~c

byte FUN_007ecdec(long param_1,int param_2,long param_3)

{
  long *plVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  
  plVar5 = (long *)(param_1 + 200);
  plVar6 = (long *)*plVar5;
  plVar7 = plVar5;
  if (plVar6 != (long *)0x0) {
    do {
      if (param_2 <= *(int *)((long)plVar6 + 0x1c)) {
        plVar7 = plVar6;
      }
      plVar6 = (long *)plVar6[*(int *)((long)plVar6 + 0x1c) < param_2];
    } while (plVar6 != (long *)0x0);
                    /* try { // try from 007ece34 to 008ece43 has its CatchHandler @ 007ee4ac */
    if ((plVar7 != plVar5) && (*(int *)((long)plVar7 + 0x1c) <= param_2)) {
      bVar2 = FUN_007ecd04();
      bVar3 = FUN_007eca30(param_1,param_2);
      bVar4 = bVar2 & bVar3;
      if (((bVar2 & 1) != 0) || ((bVar3 & 1) == 0)) goto LAB_007ece40;
      plVar8 = (long *)(param_1 + 0xe0);
      plVar6 = (long *)*plVar8;
      plVar7 = plVar8;
      plVar5 = plVar6;
      if (plVar6 != (long *)0x0) {
        do {
          if (param_2 <= (int)plVar5[4]) {
            plVar7 = plVar5;
          }
          plVar1 = plVar5 + ((int)plVar5[4] < param_2);
          plVar5 = (long *)*plVar1;
        } while ((long *)*plVar1 != (long *)0x0);
        if ((plVar7 != plVar8) && ((int)plVar7[4] <= param_2)) {
          do {
            while (param_2 < (int)plVar6[4]) {
              plVar6 = (long *)*plVar6;
              if (plVar6 == (long *)0x0) goto LAB_007ecef4;
            }
            if (param_2 <= (int)plVar6[4]) {
              bVar4 = plVar6[5] < param_3;
              goto LAB_007ece40;
            }
            plVar6 = (long *)plVar6[1];
          } while (plVar6 != (long *)0x0);
LAB_007ecef4:
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("map::at:  key not found");
        }
      }
    }
  }
  bVar4 = 1;
LAB_007ece40:
                    /* try { // try from 007ece50 to 008ed057 has its CatchHandler @ 007ee4d4 */
  return bVar4 & 1;
}

~~~
