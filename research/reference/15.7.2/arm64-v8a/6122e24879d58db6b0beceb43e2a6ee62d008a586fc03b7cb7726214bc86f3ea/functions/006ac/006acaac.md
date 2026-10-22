# 006acaac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006acaac.md)

## 関数情報

~~~json
{
  "address": "006acaac",
  "name": "FUN_006acaac",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3b26b3e8ceade784a166099da2b2daa26ad3963ef5b2badae1e902c1b0ecec2d",
  "source_text_sha256": "3b26b3e8ceade784a166099da2b2daa26ad3963ef5b2badae1e902c1b0ecec2d"
}
~~~
## 呼び出し元

- [00a82394](../00a82/00a82394.md)

## 呼び出し先

- [0063eb28](../0063e/0063eb28.md)
- [0081f580](../0081f/0081f580.md)
- [00bdb500](../00bdb/00bdb500.md)

## 疑似コード 1/1 / UTF-8 4250 bytes

~~~c

undefined8 FUN_006acaac(int *param_1)

{
  wchar_t *pwVar1;
  wchar_t *pwVar2;
  wchar_t wVar3;
  bool bVar4;
  bool bVar5;
  wchar_t wVar6;
  int iVar7;
  wchar_t wVar8;
  long lVar9;
  wchar_t *pwVar10;
  wchar_t *pwVar11;
  
  lVar9 = FUN_0081f580();
  wVar3 = *(wchar_t *)(lVar9 + (long)*param_1 * 4 + 0x49734);
  lVar9 = FUN_0081f580();
  if (*(int *)(BYTE_ARRAY_0032fef1 + lVar9 + 0x1b) == 3) {
    pwVar11 = *(wchar_t **)(param_1 + 8);
    if (pwVar11 != *(wchar_t **)(param_1 + 10)) {
      pwVar1 = *(wchar_t **)(param_1 + 0xe);
      pwVar2 = *(wchar_t **)(param_1 + 0x10);
      do {
        if (pwVar1 == pwVar2) {
          return 0;
        }
        wVar8 = *pwVar1;
        wVar6 = FUN_0063eb28(*param_1);
        if (wVar8 <= wVar6) {
          pwVar11 = *(wchar_t **)(param_1 + 10);
          pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar8,
                            (long)pwVar11 - (long)*(wchar_t **)(param_1 + 8) >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar11 = pwVar10;
          }
          if (pwVar11 == *(wchar_t **)(param_1 + 10)) break;
        }
        pwVar1 = pwVar1 + 1;
      } while( true );
    }
  }
  else {
    pwVar11 = *(wchar_t **)(param_1 + 10);
  }
  if (*(wchar_t **)(param_1 + 8) == pwVar11) {
    bVar4 = true;
  }
  else {
    pwVar1 = *(wchar_t **)(param_1 + 0x10);
    bVar4 = true;
    for (pwVar11 = *(wchar_t **)(param_1 + 0xe); pwVar11 != pwVar1; pwVar11 = pwVar11 + 1) {
      wVar8 = *pwVar11;
      wVar6 = FUN_0063eb28(*param_1);
      if (wVar8 <= wVar6) {
        pwVar2 = *(wchar_t **)(param_1 + 10);
        pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar8,
                          (long)pwVar2 - (long)*(wchar_t **)(param_1 + 8) >> 2);
        if (pwVar10 != (wchar_t *)0x0) {
          pwVar2 = pwVar10;
        }
        bVar4 = (bool)(pwVar2 != *(wchar_t **)(param_1 + 10) & bVar4);
      }
    }
  }
  pwVar11 = *(wchar_t **)(param_1 + 0xe);
  pwVar1 = *(wchar_t **)(param_1 + 0x10);
  if (pwVar11 != pwVar1) {
    bVar5 = false;
    do {
                    /* catch() { ... } // from try @ 006acc94 with catch @ 006acbf4 */
      wVar8 = *pwVar11;
      wVar6 = FUN_0063eb28(*param_1);
      if (wVar8 <= wVar6) {
        if (wVar3 == wVar8) {
          if (bVar4) {
            return 0;
          }
          pwVar10 = *(wchar_t **)(param_1 + 8);
          pwVar2 = *(wchar_t **)(param_1 + 10);
          if (pwVar10 == pwVar2) {
            return 0;
          }
          pwVar10 = wmemchr(pwVar10,wVar3,(long)pwVar2 - (long)pwVar10 >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar2 = pwVar10;
          }
          if (pwVar2 == *(wchar_t **)(param_1 + 10)) {
            return 0;
          }
        }
        bVar5 = true;
      }
      pwVar11 = pwVar11 + 1;
    } while (pwVar11 != pwVar1);
    if (bVar5) {
      return 1;
    }
  }
  lVar9 = FUN_0081f580();
  if (*(int *)(BYTE_ARRAY_0032fef1 + lVar9 + 0x1b) == 7) {
    iVar7 = FUN_0063eb28(*param_1);
    if (iVar7 < 2) {
      return 0;
    }
    if (L'\x01' < wVar3) {
      return 0;
    }
                    /* try { // try from 006acc88 to 007acc93 has its CatchHandler @ 006acd1c */
    if (*(long *)(param_1 + 8) != *(long *)(param_1 + 10)) {
                    /* try { // try from 006acc94 to 007acdaf has its CatchHandler @ 006acbf4 */
      pwVar11 = *(wchar_t **)(param_1 + 0xe);
      pwVar1 = *(wchar_t **)(param_1 + 0x10);
      if (pwVar11 == pwVar1) {
        return 1;
      }
      do {
        wVar3 = *pwVar11;
        wVar8 = FUN_0063eb28(*param_1);
        if (wVar3 <= wVar8) {
          pwVar2 = *(wchar_t **)(param_1 + 10);
          pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar3,
                            (long)pwVar2 - (long)*(wchar_t **)(param_1 + 8) >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar2 = pwVar10;
          }
          if (pwVar2 == *(wchar_t **)(param_1 + 10)) {
            return 0;
          }
        }
        pwVar11 = pwVar11 + 1;
        if (pwVar11 == pwVar1) {
          return 1;
        }
      } while( true );
    }
  }
  return 0;
}

~~~
