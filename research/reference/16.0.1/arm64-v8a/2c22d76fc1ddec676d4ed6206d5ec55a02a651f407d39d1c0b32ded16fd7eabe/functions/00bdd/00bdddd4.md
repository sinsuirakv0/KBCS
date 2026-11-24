# 00bdddd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd9ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-10f86b6bdaf455e240684731e466ca0b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdde70`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-bec1de1c10f998035360c941bf5ad41d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddd4",
  "name": "_ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c0e6ef6bf02f13059bdcaad4210353d0f35f1bcd726196cafd3b5adb004f949",
  "source_text_sha256": "5c0e6ef6bf02f13059bdcaad4210353d0f35f1bcd726196cafd3b5adb004f949",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddd4",
        "00bdde43"
      ]
    ],
    "bytes_sha256": "4732fd065bc72d3f303b166e36bb0fbdbb40ad24af71f7d77b02796d27edd05e",
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
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126e28 == 0) {
    DAT_01126e28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
                    /* try { // try from 00bdde14 to 00cdde1f has its CatchHandler @ 00bdeecc */
  }
                    /* try { // try from 00bdde20 to 00cdea5f has its CatchHandler @ 00bd6f4c */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126e28,&DAT_00310230,1,&DAT_01126e58,
             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddd4"></a> `00bdddd4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdddd8"></a> `00bdddd8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddddc"></a> `00bddddc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddde0"></a> `00bddde0` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddde4"></a> `00bddde4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bddde8"></a> `00bddde8` | `81 16 47 f9` | ldr x1,[x20, #0xe28] | `FALL_THROUGH`
<a id="insn-00bdddec"></a> `00bdddec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdddf0"></a> `00bdddf0` | `41 01 00 b5` | cbnz x1,0x00bdde18 | `CONDITIONAL_JUMP`
<a id="insn-00bdddf4"></a> `00bdddf4` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `63 20 12 91` | add x3,x3,#0x488 | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdde00"></a> `00bdde00` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdde04"></a> `00bdde04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdde08"></a> `00bdde08` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdde0c"></a> `00bdde0c` | `41 f4 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdde10"></a> `00bdde10` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdde14"></a> `00bdde14` | `80 16 07 f9` | str x0,[x20, #0xe28] | `FALL_THROUGH`
<a id="insn-00bdde18"></a> `00bdde18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdde1c"></a> `00bdde1c` | `82 b9 ff f0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdde20"></a> `00bdde20` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdde24"></a> `00bdde24` | `85 b6 ff 90` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdde28"></a> `00bdde28` | `42 c0 08 91` | add x2,x2,#0x230 | `FALL_THROUGH`
<a id="insn-00bdde2c"></a> `00bdde2c` | `84 60 39 91` | add x4,x4,#0xe58 | `FALL_THROUGH`
<a id="insn-00bdde30"></a> `00bdde30` | `a5 20 12 91` | add x5,x5,#0x488 | `FALL_THROUGH`
<a id="insn-00bdde34"></a> `00bdde34` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdde38"></a> `00bdde38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdde3c"></a> `00bdde3c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdde40"></a> `00bdde40` | `2c f4 01 14` | b 0x00c5aef0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddd4`](#insn-00bdddd4) 範囲 `[['00bdddd4', '00bdddf3']]`
  - `CONDITIONAL_JUMP` [`00bdddf0`](#insn-00bdddf0) → [`00bdde18`](#insn-00bdde18)
  - `FALL_THROUGH` [`00bdddf0`](#insn-00bdddf0) → [`00bdddf4`](#insn-00bdddf4)
- ブロック [`00bdddf4`](#insn-00bdddf4) 範囲 `[['00bdddf4', '00bdde13']]`
  - `FALL_THROUGH` [`00bdde10`](#insn-00bdde10) → [`00bdde14`](#insn-00bdde14)
- ブロック [`00bdde14`](#insn-00bdde14) 範囲 `[['00bdde14', '00bdde17']]`
  - `FALL_THROUGH` [`00bdde14`](#insn-00bdde14) → [`00bdde18`](#insn-00bdde18)
- ブロック [`00bdde18`](#insn-00bdde18) 範囲 `[['00bdde18', '00bdde1f']]`
  - `FALL_THROUGH` [`00bdde1c`](#insn-00bdde1c) → [`00bdde20`](#insn-00bdde20)
- ブロック [`00bdde20`](#insn-00bdde20) 範囲 `[['00bdde20', '00bdde43']]`

## 命令位置別の参照

- [`00bdddd4`](#insn-00bdddd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddd8`](#insn-00bdddd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddde8`](#insn-00bddde8) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdddf0`](#insn-00bdddf0) → [`00bdde18`](#insn-00bdde18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddf8`](#insn-00bdddf8) → `002ad488`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdde0c`](#insn-00bdde0c) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bdde14`](#insn-00bdde14) → `01126e28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdde18`](#insn-00bdde18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde28`](#insn-00bdde28) → `00310230`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde2c`](#insn-00bdde2c) → `01126e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde30`](#insn-00bdde30) → `002ad488`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdde40`](#insn-00bdde40) → [`00c5aef0`](../00c5a/00c5aef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aef0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddd4`](#insn-00bdddd4)

~~~json
{
  "source": "00bdddd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddd8`](#insn-00bdddd8)

~~~json
{
  "source": "00bdddd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddde8`](#insn-00bddde8)

~~~json
{
  "source": "00bddde8",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdddf0`](#insn-00bdddf0)

~~~json
{
  "source": "00bdddf0",
  "target": "00bdde18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddf8`](#insn-00bdddf8)

~~~json
{
  "source": "00bdddf8",
  "target": "002ad488",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad484",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad484",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdde0c`](#insn-00bdde0c)

~~~json
{
  "source": "00bdde0c",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdde14`](#insn-00bdde14)

~~~json
{
  "source": "00bdde14",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdde18`](#insn-00bdde18)

~~~json
{
  "source": "00bdde18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde28`](#insn-00bdde28)

~~~json
{
  "source": "00bdde28",
  "target": "00310230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde2c`](#insn-00bdde2c)

~~~json
{
  "source": "00bdde2c",
  "target": "01126e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde30`](#insn-00bdde30)

~~~json
{
  "source": "00bdde30",
  "target": "002ad488",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad484",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad484",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdde40`](#insn-00bdde40)

~~~json
{
  "source": "00bdde40",
  "target": "00c5aef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
