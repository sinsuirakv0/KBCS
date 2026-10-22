# 00b5accc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b5accc.md)

## 関数情報

~~~json
{
  "address": "00b5accc",
  "name": "firebase::auth::Auth::FindAuth",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77b0e5fc53574aeb37b0138f7416cb2bff34ed7206b936a7cf4fecb9bda7e0cb",
  "source_text_sha256": "77b0e5fc53574aeb37b0138f7416cb2bff34ed7206b936a7cf4fecb9bda7e0cb"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード 1/1 / UTF-8 1185 bytes

~~~c

/* firebase::auth::Auth::FindAuth(firebase::App*) */

undefined8 firebase::auth::Auth::FindAuth(App *param_1)

{
  undefined *puVar1;
  undefined *puVar2;
  Mutex *this;
  undefined8 uVar3;
  
  this = *(Mutex **)PTR_g_auths_mutex_00c1ba70;
                    /* try { // try from 00b5acec to 00c5acff has its CatchHandler @ 00b5ae88 */
  Mutex::Acquire(this);
  puVar2 = *(undefined **)(PTR_g_auths_00c1ba78 + 8);
  if (puVar2 != (undefined *)0x0) {
    puVar1 = PTR_g_auths_00c1ba78 + 8;
    do {
      if (*(App **)(puVar2 + 0x20) >= param_1) {
        puVar1 = puVar2;
      }
      puVar2 = *(undefined **)(puVar2 + (ulong)(*(App **)(puVar2 + 0x20) < param_1) * 8);
    } while (puVar2 != (undefined *)0x0);
    if ((puVar1 != PTR_g_auths_00c1ba78 + 8) && (*(App **)(puVar1 + 0x20) <= param_1)) {
      uVar3 = *(undefined8 *)(puVar1 + 0x28);
      goto LAB_00b5ad38;
    }
  }
                    /* try { // try from 00b5ad34 to 00c5ad43 has its CatchHandler @ 00b5aea4 */
  uVar3 = 0;
LAB_00b5ad38:
  Mutex::Release(this);
                    /* try { // try from 00b5ad44 to 00c5ad57 has its CatchHandler @ 00b5ae8c */
  return uVar3;
}

~~~
