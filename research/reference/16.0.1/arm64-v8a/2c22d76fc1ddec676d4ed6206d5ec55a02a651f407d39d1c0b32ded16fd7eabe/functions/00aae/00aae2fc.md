# 00aae2fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aae2fc",
  "name": "FUN_00aae2fc",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cfcce6eb5e4d302d7b7ca5490f187d54db72c75c911cbc87f7b96f448dca72af",
  "source_text_sha256": "cfcce6eb5e4d302d7b7ca5490f187d54db72c75c911cbc87f7b96f448dca72af"
}
~~~

## 呼び出し元

- [00aae1cc](../00aae/00aae1cc.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3488 bytes

~~~c

long * FUN_00aae2fc(undefined8 *param_1,long *param_2,long *param_3,long *param_4,int *param_5)

{
  int iVar1;
  bool bVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar4 = param_1 + 1;
  if (plVar4 != param_2) {
    iVar1 = *param_5;
    if ((int)param_2[4] <= iVar1) {
      if (iVar1 <= (int)param_2[4]) {
        *param_3 = (long)param_2;
        *param_4 = (long)param_2;
        return param_4;
      }
      plVar6 = (long *)param_2[1];
      plVar7 = param_2;
      plVar5 = plVar6;
      if (plVar6 == (long *)0x0) {
        do {
          plVar3 = (long *)plVar7[2];
          bVar2 = (long *)*plVar3 != plVar7;
          plVar7 = plVar3;
        } while (bVar2);
      }
      else {
        do {
          plVar3 = plVar5;
                    /* try { // try from 00aae360 to 00bae37b has its CatchHandler @ 00aae8dc */
          plVar5 = (long *)*plVar3;
        } while ((long *)*plVar3 != (long *)0x0);
      }
                    /* try { // try from 00aae428 to 00bae44b has its CatchHandler @ 00aae7c4 */
      if ((plVar3 == plVar4) || (iVar1 < (int)plVar3[4])) {
        if (plVar6 != (long *)0x0) {
          *param_3 = (long)plVar3;
          return plVar3;
        }
        *param_3 = (long)param_2;
        return param_2 + 1;
      }
                    /* try { // try from 00aae44c to 00bae467 has its CatchHandler @ 00aae26c */
      plVar5 = (long *)*plVar4;
      plVar7 = plVar4;
      while (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae468 to 00bae46f has its CatchHandler @ 00aae87c */
        while (plVar7 = plVar5, iVar1 < (int)plVar7[4]) {
          plVar4 = plVar7;
          plVar5 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00aae48c;
        }
        if (iVar1 <= (int)plVar7[4]) break;
        plVar4 = plVar7 + 1;
        plVar5 = (long *)*plVar4;
      }
LAB_00aae48c:
      *param_3 = (long)plVar7;
      return plVar4;
    }
  }
  plVar5 = (long *)*param_2;
  plVar7 = param_2;
  if ((long *)*param_1 != param_2) {
    plVar6 = param_2;
    plVar3 = plVar5;
    if (plVar5 == (long *)0x0) {
      do {
        plVar7 = (long *)plVar6[2];
        bVar2 = (long *)*plVar7 == plVar6;
        plVar6 = plVar7;
      } while (bVar2);
    }
    else {
      do {
                    /* try { // try from 00aae330 to 00bae35f has its CatchHandler @ 00aae26c */
        plVar7 = plVar3;
        plVar3 = (long *)plVar7[1];
      } while ((long *)plVar7[1] != (long *)0x0);
    }
    iVar1 = *param_5;
                    /* try { // try from 00aae390 to 00bae39b has its CatchHandler @ 00aae7d4 */
    if (iVar1 <= (int)plVar7[4]) {
      plVar5 = (long *)*plVar4;
      plVar7 = plVar4;
      while (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae3d0 to 00bae3f7 has its CatchHandler @ 00aae7cc */
        while (plVar7 = plVar5, iVar1 < (int)plVar7[4]) {
          plVar4 = plVar7;
          plVar5 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00aae3e8;
        }
        if (iVar1 <= (int)plVar7[4]) break;
        plVar4 = plVar7 + 1;
        plVar5 = (long *)*plVar4;
      }
LAB_00aae3e8:
      *param_3 = (long)plVar7;
      return plVar4;
    }
  }
  if (plVar5 != (long *)0x0) {
                    /* try { // try from 00aae39c to 00bae3cf has its CatchHandler @ 00aae26c */
    *param_3 = (long)plVar7;
    return plVar7 + 1;
  }
  *param_3 = (long)param_2;
  return param_2;
}

~~~
