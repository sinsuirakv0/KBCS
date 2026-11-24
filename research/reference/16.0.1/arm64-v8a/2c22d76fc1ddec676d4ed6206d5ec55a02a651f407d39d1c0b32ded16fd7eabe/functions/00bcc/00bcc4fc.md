# 00bcc4fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc0d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-1f4d995c5cfcb36e46637ed0d637d79b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcc598`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc598.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-cb2d2ba80165a442373e38c22f39fb68)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc4fc",
  "name": "_ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4fae8c1e5e1801db08dc45383f23bed12faeec42f2d7dd68f35ec916acea1b5f",
  "source_text_sha256": "4fae8c1e5e1801db08dc45383f23bed12faeec42f2d7dd68f35ec916acea1b5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc4fc",
        "00bcc56b"
      ]
    ],
    "bytes_sha256": "d6547852a34e196a5018c6c28b912d87abb19b1e77087e2241222e5892cc3696",
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

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 754 bytes

~~~c

void _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* catch() { ... } // from try @ 00bcc394 with catch @ 00bcc500 */
  if (DAT_01126728 == 0) {
    DAT_01126728 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126728,&PTR_s_getInstance_00c91988,0x12,&DAT_01126738,
             "com/google/firebase/auth/FirebaseAuth");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc4fc"></a> `00bcc4fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcc500"></a> `00bcc500` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc504"></a> `00bcc504` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc508"></a> `00bcc508` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc50c"></a> `00bcc50c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bcc510"></a> `00bcc510` | `81 96 43 f9` | ldr x1,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00bcc514"></a> `00bcc514` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcc518"></a> `00bcc518` | `41 01 00 b5` | cbnz x1,0x00bcc540 | `CONDITIONAL_JUMP`
<a id="insn-00bcc51c"></a> `00bcc51c` | `03 b7 ff 90` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcc520"></a> `00bcc520` | `63 f0 08 91` | add x3,x3,#0x23c | `FALL_THROUGH`
<a id="insn-00bcc524"></a> `00bcc524` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc528"></a> `00bcc528` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bcc52c"></a> `00bcc52c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcc530"></a> `00bcc530` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcc534"></a> `00bcc534` | `77 3a 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc538"></a> `00bcc538` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bcc53c"></a> `00bcc53c` | `80 96 03 f9` | str x0,[x20, #0x728] | `FALL_THROUGH`
<a id="insn-00bcc540"></a> `00bcc540` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc544"></a> `00bcc544` | `22 06 00 b0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bcc548"></a> `00bcc548` | `c4 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc54c"></a> `00bcc54c` | `05 b7 ff 90` | adrp x5,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcc550"></a> `00bcc550` | `42 20 26 91` | add x2,x2,#0x988 | `FALL_THROUGH`
<a id="insn-00bcc554"></a> `00bcc554` | `84 e0 1c 91` | add x4,x4,#0x738 | `FALL_THROUGH`
<a id="insn-00bcc558"></a> `00bcc558` | `a5 f0 08 91` | add x5,x5,#0x23c | `FALL_THROUGH`
<a id="insn-00bcc55c"></a> `00bcc55c` | `43 02 80 52` | mov w3,#0x12 | `FALL_THROUGH`
<a id="insn-00bcc560"></a> `00bcc560` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc564"></a> `00bcc564` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc568"></a> `00bcc568` | `72 3a 02 14` | b 0x00c5af30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc4fc`](#insn-00bcc4fc) 範囲 `[['00bcc4fc', '00bcc4ff']]`
  - `FALL_THROUGH` [`00bcc4fc`](#insn-00bcc4fc) → [`00bcc500`](#insn-00bcc500)
- ブロック [`00bcc500`](#insn-00bcc500) 範囲 `[['00bcc500', '00bcc51b']]`
  - `CONDITIONAL_JUMP` [`00bcc518`](#insn-00bcc518) → [`00bcc540`](#insn-00bcc540)
  - `FALL_THROUGH` [`00bcc518`](#insn-00bcc518) → [`00bcc51c`](#insn-00bcc51c)
- ブロック [`00bcc51c`](#insn-00bcc51c) 範囲 `[['00bcc51c', '00bcc53f']]`
  - `FALL_THROUGH` [`00bcc53c`](#insn-00bcc53c) → [`00bcc540`](#insn-00bcc540)
- ブロック [`00bcc540`](#insn-00bcc540) 範囲 `[['00bcc540', '00bcc56b']]`

## 命令位置別の参照

- [`00bcc4fc`](#insn-00bcc4fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc500`](#insn-00bcc500) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc510`](#insn-00bcc510) → `01126728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc518`](#insn-00bcc518) → [`00bcc540`](#insn-00bcc540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc520`](#insn-00bcc520) → `002ac23c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc534`](#insn-00bcc534) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bcc53c`](#insn-00bcc53c) → `01126728`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc540`](#insn-00bcc540) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc550`](#insn-00bcc550) → `00c91988`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcc554`](#insn-00bcc554) → `01126738`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc558`](#insn-00bcc558) → `002ac23c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc568`](#insn-00bcc568) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc4fc`](#insn-00bcc4fc)

~~~json
{
  "source": "00bcc4fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc500`](#insn-00bcc500)

~~~json
{
  "source": "00bcc500",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc510`](#insn-00bcc510)

~~~json
{
  "source": "00bcc510",
  "target": "01126728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc518`](#insn-00bcc518)

~~~json
{
  "source": "00bcc518",
  "target": "00bcc540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc520`](#insn-00bcc520)

~~~json
{
  "source": "00bcc520",
  "target": "002ac23c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac238",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac238",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcc534`](#insn-00bcc534)

~~~json
{
  "source": "00bcc534",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc53c`](#insn-00bcc53c)

~~~json
{
  "source": "00bcc53c",
  "target": "01126728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc540`](#insn-00bcc540)

~~~json
{
  "source": "00bcc540",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc550`](#insn-00bcc550)

~~~json
{
  "source": "00bcc550",
  "target": "00c91988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91988",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcc554`](#insn-00bcc554)

~~~json
{
  "source": "00bcc554",
  "target": "01126738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126738",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc558`](#insn-00bcc558)

~~~json
{
  "source": "00bcc558",
  "target": "002ac23c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac238",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac238",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcc568`](#insn-00bcc568)

~~~json
{
  "source": "00bcc568",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
