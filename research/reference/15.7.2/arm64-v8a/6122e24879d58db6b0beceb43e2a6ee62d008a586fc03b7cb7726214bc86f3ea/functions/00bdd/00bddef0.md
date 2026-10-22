# 00bddef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddef0.md)

## 関数情報

~~~json
{
  "address": "00bddef0",
  "name": "firebase::ReferenceCountedFutureImpl::SetBackingError",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eff941e342220f528ad1bbe46d0542b9377d2e11a68f81f579679723477ce6bd",
  "source_text_sha256": "eff941e342220f528ad1bbe46d0542b9377d2e11a68f81f579679723477ce6bd"
}
~~~
## 呼び出し元

- [00ae348c](../00ae3/00ae348c.md)
- [00ae3ab8](../00ae3/00ae3ab8.md)
- [00ae3bdc](../00ae3/00ae3bdc.md)
- [00ae3d44](../00ae3/00ae3d44.md)
- [00b59f90](../00b59/00b59f90.md)
- [00b5a0bc](../00b5a/00b5a0bc.md)
- [00b5a1ec](../00b5a/00b5a1ec.md)
- [00b5a3a0](../00b5a/00b5a3a0.md)
- [00b5fef0](../00b5f/00b5fef0.md)
- [00b600cc](../00b60/00b600cc.md)
- [00b603e4](../00b60/00b603e4.md)
- [00b605d0](../00b60/00b605d0.md)
- [00b607ac](../00b60/00b607ac.md)
- [00b60984](../00b60/00b60984.md)
- [00b60b60](../00b60/00b60b60.md)
- [00b6ca20](../00b6c/00b6ca20.md)
- [00b6d224](../00b6d/00b6d224.md)
- [00b71878](../00b71/00b71878.md)
- [00b71a54](../00b71/00b71a54.md)

## 呼び出し先

- [00aff110](../00aff/00aff110.md)

## 疑似コード 1/1 / UTF-8 260 bytes

~~~c

void __thiscall
firebase::ReferenceCountedFutureImpl::SetBackingError
          (ReferenceCountedFutureImpl *this,FutureBackingData *param_1,int param_2,char *param_3)

{
  (*(code *)PTR_SetBackingError_00c1d7b0)(this,param_1,param_2);
  return;
}

~~~
