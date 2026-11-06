# 00bdecc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdecc0.md)

## 関数情報

~~~json
{
  "address": "00bdecc0",
  "name": "<EXTERNAL>::sem_post",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5beec4a18e7ae7eecb227ceae947bbc613852ab6b8b7f82c11149f7779d10e37",
  "source_text_sha256": "5beec4a18e7ae7eecb227ceae947bbc613852ab6b8b7f82c11149f7779d10e37"
}
~~~
## 呼び出し元

- [00afc3b8](../00afc/00afc3b8.md)
- [00afc40c](../00afc/00afc40c.md)

## 呼び出し先

- [010a55e0](../010a5/010a55e0.md)

## 疑似コード 1/1 / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_post(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_post_00c1df18)((int)__sem);
  return iVar1;
}

~~~
