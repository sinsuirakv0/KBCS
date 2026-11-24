# 00bb8efc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb8ad4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ad4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-7c5187c9baa11d44f4b15a34399942a4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb8f98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-8386f65ae9f3d0f5981c3a4488dace8b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8efc",
  "name": "_ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c14bc2e1e6cf56065e229b72954431c98005b5b3ae1aa1ec2d0a36262e0d88d3",
  "source_text_sha256": "c14bc2e1e6cf56065e229b72954431c98005b5b3ae1aa1ec2d0a36262e0d88d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8efc",
        "00bb8f6b"
      ]
    ],
    "bytes_sha256": "8551651520a34ab4df8c94d22ade61d31f64085a8b2d087e22e64d39d85bc277",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aef0](../00c5a/00c5aef0.md)
- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 881 bytes

~~~c

void _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011262a8 == 0) {
                    /* try { // try from 00bb8f2c to 00cb8f3b has its CatchHandler @ 00bb909c */
    DAT_011262a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
                    /* try { // try from 00bb8f3c to 00cb8f4f has its CatchHandler @ 00bb9084 */
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_011262a8,&DAT_0030e730,1,&DAT_01126310,
             "com/google/firebase/messaging/FirebaseMessaging");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb8efc"></a> `00bb8efc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb8f00"></a> `00bb8f00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8f04"></a> `00bb8f04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bb8f08"></a> `00bb8f08` | `74 2b 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8f0c"></a> `00bb8f0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bb8f10"></a> `00bb8f10` | `81 56 41 f9` | ldr x1,[x20, #0x2a8] | `FALL_THROUGH`
<a id="insn-00bb8f14"></a> `00bb8f14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb8f18"></a> `00bb8f18` | `41 01 00 b5` | cbnz x1,0x00bb8f40 | `CONDITIONAL_JUMP`
<a id="insn-00bb8f1c"></a> `00bb8f1c` | `03 b8 ff d0` | adrp x3,0x2ba000 | `FALL_THROUGH`
<a id="insn-00bb8f20"></a> `00bb8f20` | `63 78 3a 91` | add x3,x3,#0xe9e | `FALL_THROUGH`
<a id="insn-00bb8f24"></a> `00bb8f24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb8f28"></a> `00bb8f28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bb8f2c"></a> `00bb8f2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bb8f30"></a> `00bb8f30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bb8f34"></a> `00bb8f34` | `f7 87 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8f38"></a> `00bb8f38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bb8f3c"></a> `00bb8f3c` | `80 56 01 f9` | str x0,[x20, #0x2a8] | `FALL_THROUGH`
<a id="insn-00bb8f40"></a> `00bb8f40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8f44"></a> `00bb8f44` | `a2 ba ff d0` | adrp x2,0x30e000 | `FALL_THROUGH`
<a id="insn-00bb8f48"></a> `00bb8f48` | `64 2b 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8f4c"></a> `00bb8f4c` | `05 b8 ff d0` | adrp x5,0x2ba000 | `FALL_THROUGH`
<a id="insn-00bb8f50"></a> `00bb8f50` | `42 c0 1c 91` | add x2,x2,#0x730 | `FALL_THROUGH`
<a id="insn-00bb8f54"></a> `00bb8f54` | `84 40 0c 91` | add x4,x4,#0x310 | `FALL_THROUGH`
<a id="insn-00bb8f58"></a> `00bb8f58` | `a5 78 3a 91` | add x5,x5,#0xe9e | `FALL_THROUGH`
<a id="insn-00bb8f5c"></a> `00bb8f5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bb8f60"></a> `00bb8f60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb8f64"></a> `00bb8f64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb8f68"></a> `00bb8f68` | `e2 87 02 14` | b 0x00c5aef0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8efc`](#insn-00bb8efc) 範囲 `[['00bb8efc', '00bb8f1b']]`
  - `CONDITIONAL_JUMP` [`00bb8f18`](#insn-00bb8f18) → [`00bb8f40`](#insn-00bb8f40)
  - `FALL_THROUGH` [`00bb8f18`](#insn-00bb8f18) → [`00bb8f1c`](#insn-00bb8f1c)
- ブロック [`00bb8f1c`](#insn-00bb8f1c) 範囲 `[['00bb8f1c', '00bb8f2b']]`
  - `FALL_THROUGH` [`00bb8f28`](#insn-00bb8f28) → [`00bb8f2c`](#insn-00bb8f2c)
- ブロック [`00bb8f2c`](#insn-00bb8f2c) 範囲 `[['00bb8f2c', '00bb8f3b']]`
  - `FALL_THROUGH` [`00bb8f38`](#insn-00bb8f38) → [`00bb8f3c`](#insn-00bb8f3c)
- ブロック [`00bb8f3c`](#insn-00bb8f3c) 範囲 `[['00bb8f3c', '00bb8f3f']]`
  - `FALL_THROUGH` [`00bb8f3c`](#insn-00bb8f3c) → [`00bb8f40`](#insn-00bb8f40)
- ブロック [`00bb8f40`](#insn-00bb8f40) 範囲 `[['00bb8f40', '00bb8f6b']]`

## 命令位置別の参照

- [`00bb8efc`](#insn-00bb8efc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f00`](#insn-00bb8f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f10`](#insn-00bb8f10) → `011262a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8f18`](#insn-00bb8f18) → [`00bb8f40`](#insn-00bb8f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f20`](#insn-00bb8f20) → `002bae9e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb8f34`](#insn-00bb8f34) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f3c`](#insn-00bb8f3c) → `011262a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8f40`](#insn-00bb8f40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f50`](#insn-00bb8f50) → `0030e730`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f54`](#insn-00bb8f54) → `01126310`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f58`](#insn-00bb8f58) → `002bae9e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb8f68`](#insn-00bb8f68) → [`00c5aef0`](../00c5a/00c5aef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aef0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8efc`](#insn-00bb8efc)

~~~json
{
  "source": "00bb8efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f00`](#insn-00bb8f00)

~~~json
{
  "source": "00bb8f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f10`](#insn-00bb8f10)

~~~json
{
  "source": "00bb8f10",
  "target": "011262a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8f18`](#insn-00bb8f18)

~~~json
{
  "source": "00bb8f18",
  "target": "00bb8f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f20`](#insn-00bb8f20)

~~~json
{
  "source": "00bb8f20",
  "target": "002bae9e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bae9a",
  "offset": 4,
  "size": 52,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002bae9a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb8f34`](#insn-00bb8f34)

~~~json
{
  "source": "00bb8f34",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8f3c`](#insn-00bb8f3c)

~~~json
{
  "source": "00bb8f3c",
  "target": "011262a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8f40`](#insn-00bb8f40)

~~~json
{
  "source": "00bb8f40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f50`](#insn-00bb8f50)

~~~json
{
  "source": "00bb8f50",
  "target": "0030e730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f54`](#insn-00bb8f54)

~~~json
{
  "source": "00bb8f54",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f58`](#insn-00bb8f58)

~~~json
{
  "source": "00bb8f58",
  "target": "002bae9e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bae9a",
  "offset": 4,
  "size": 52,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002bae9a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb8f68`](#insn-00bb8f68)

~~~json
{
  "source": "00bb8f68",
  "target": "00c5aef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
