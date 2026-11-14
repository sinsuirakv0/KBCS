# 009ddecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009ddecc",
  "name": "FUN_009ddecc",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09b0168f8df72c77ddbe4933917289a30937a23d1bca523b6dace51e58ac7ff6",
  "source_text_sha256": "09b0168f8df72c77ddbe4933917289a30937a23d1bca523b6dace51e58ac7ff6"
}
~~~

## 呼び出し元

- [0063b0a4](../0063b/0063b0a4.md)
- [0063b93c](../0063b/0063b93c.md)
- [0063c088](../0063c/0063c088.md)
- [0064f0a8](../0064f/0064f0a8.md)
- [006c1340](../006c1/006c1340.md)
- [006c15a4](../006c1/006c15a4.md)
- [006c2420](../006c2/006c2420.md)
- [006d4244](../006d4/006d4244.md)
- [006dd66c](../006dd/006dd66c.md)
- [006deb90](../006de/006deb90.md)
- [006dee9c](../006de/006dee9c.md)
- [006e22b0](../006e2/006e22b0.md)
- [006e3728](../006e3/006e3728.md)
- [006f28dc](../006f2/006f28dc.md)
- [0076a1b8](../0076a/0076a1b8.md)
- [008dd120](../008dd/008dd120.md)
- [008e76ac](../008e7/008e76ac.md)
- [008f09f4](../008f0/008f09f4.md)
- [008f4044](../008f4/008f4044.md)
- [0098ec08](../0098e/0098ec08.md)
- [00a76e10](../00a76/00a76e10.md)

## 呼び出し先

- [0085c2a8](../0085c/0085c2a8.md)
- [0085c2b0](../0085c/0085c2b0.md)
- [0085c2b8](../0085c/0085c2b8.md)
- [0085c2c0](../0085c/0085c2c0.md)

## 疑似コード / UTF-8 1529 bytes

~~~c

undefined8 FUN_009ddecc(undefined8 param_1,int param_2,int param_3,int param_4,int param_5)

{
  int iVar1;
  
                    /* try { // try from 009ddee8 to 00addeef has its CatchHandler @ 009ddfd4 */
  iVar1 = FUN_0085c2a8();
  if (param_2 <= iVar1) {
                    /* try { // try from 009ddf04 to 00addf23 has its CatchHandler @ 009ddfec */
    iVar1 = FUN_0085c2a8(param_1);
    if ((iVar1 <= param_4 + param_2) && (iVar1 = FUN_0085c2b0(param_1), param_3 <= iVar1)) {
      iVar1 = FUN_0085c2b0(param_1);
                    /* try { // try from 009ddf38 to 00addf3f has its CatchHandler @ 009ddfb0 */
                    /* try { // try from 009ddf54 to 00addf5b has its CatchHandler @ 009ddf60 */
                    /* catch() { ... } // from try @ 009ddc3c with catch @ 009ddf5c
                       try { // try from 009ddf5c to 00ade02f has its CatchHandler @ 009dd934 */
                    /* catch() { ... } // from try @ 009ddc08 with catch @ 009ddf60
                       catch() { ... } // from try @ 009ddf54 with catch @ 009ddf60 */
      if (((iVar1 <= param_5 + param_3) &&
          (((iVar1 = FUN_0085c2b8(param_1), param_2 <= iVar1 &&
            (iVar1 = FUN_0085c2b8(param_1), iVar1 <= param_4 + param_2)) &&
           (iVar1 = FUN_0085c2c0(param_1), param_3 <= iVar1)))) &&
         (iVar1 = FUN_0085c2c0(param_1), iVar1 <= param_5 + param_3)) {
        return 1;
      }
    }
  }
                    /* catch() { ... } // from try @ 009dde44 with catch @ 009ddf78 */
  return 0;
}

~~~
