# 00ae6fdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae70a4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-43c0627a0f524972912cb8d0d1b8b638)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6fdc",
  "name": "_ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf0b71d6b167d4403c1ab6efd90586c8ae60185281a3b6fb61665b4c60d52cbf",
  "source_text_sha256": "cf0b71d6b167d4403c1ab6efd90586c8ae60185281a3b6fb61665b4c60d52cbf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae6fdc",
        "00ae704b"
      ]
    ],
    "bytes_sha256": "31082a1e1200551aefa66ddf57797e1bef780ebfcfc9641d6ed8f7a9179d5958",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"android/content/res/Resources"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 849 bytes

~~~c

void _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00ae6fdc to 00be6fdf has its CatchHandler @ 00ae8d24 */
                    /* try { // try from 00ae6fe0 to 00be7083 has its CatchHandler @ 00ae6000 */
  if (DAT_010a03e8 == 0) {
    DAT_010a03e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/content/res/Resources",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a03e8,&PTR_s_getIdentifier_00c0fd48,1,&DAT_010a03f8,
             "android/content/res/Resources");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae6fdc"></a> `00ae6fdc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae6fe0"></a> `00ae6fe0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6fe4"></a> `00ae6fe4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae6fe8"></a> `00ae6fe8` | `d4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6fec"></a> `00ae6fec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae6ff0"></a> `00ae6ff0` | `81 f6 41 f9` | ldr x1,[x20, #0x3e8] | `FALL_THROUGH`
<a id="insn-00ae6ff4"></a> `00ae6ff4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae6ff8"></a> `00ae6ff8` | `41 01 00 b5` | cbnz x1,0x00ae7020 | `CONDITIONAL_JUMP`
<a id="insn-00ae6ffc"></a> `00ae6ffc` | `e3 bd ff d0` | adrp x3,0x2a4000 | `FALL_THROUGH`
<a id="insn-00ae7000"></a> `00ae7000` | `63 60 39 91` | add x3,x3,#0xe58 | `FALL_THROUGH`
<a id="insn-00ae7004"></a> `00ae7004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7008"></a> `00ae7008` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae700c"></a> `00ae700c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae7010"></a> `00ae7010` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae7014"></a> `00ae7014` | `df db 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae7018"></a> `00ae7018` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ae701c"></a> `00ae701c` | `80 f6 01 f9` | str x0,[x20, #0x3e8] | `FALL_THROUGH`
<a id="insn-00ae7020"></a> `00ae7020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7024"></a> `00ae7024` | `42 09 00 90` | adrp x2,0xc0f000 | `FALL_THROUGH`
<a id="insn-00ae7028"></a> `00ae7028` | `c4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae702c"></a> `00ae702c` | `e5 bd ff b0` | adrp x5,0x2a4000 | `FALL_THROUGH`
<a id="insn-00ae7030"></a> `00ae7030` | `42 20 35 91` | add x2,x2,#0xd48 | `FALL_THROUGH`
<a id="insn-00ae7034"></a> `00ae7034` | `84 e0 0f 91` | add x4,x4,#0x3f8 | `FALL_THROUGH`
<a id="insn-00ae7038"></a> `00ae7038` | `a5 60 39 91` | add x5,x5,#0xe58 | `FALL_THROUGH`
<a id="insn-00ae703c"></a> `00ae703c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ae7040"></a> `00ae7040` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7044"></a> `00ae7044` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae7048"></a> `00ae7048` | `da db 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae6fdc`](#insn-00ae6fdc) 範囲 `[['00ae6fdc', '00ae6fdf']]`
  - `FALL_THROUGH` [`00ae6fdc`](#insn-00ae6fdc) → [`00ae6fe0`](#insn-00ae6fe0)
- ブロック [`00ae6fe0`](#insn-00ae6fe0) 範囲 `[['00ae6fe0', '00ae6ffb']]`
  - `CONDITIONAL_JUMP` [`00ae6ff8`](#insn-00ae6ff8) → [`00ae7020`](#insn-00ae7020)
  - `FALL_THROUGH` [`00ae6ff8`](#insn-00ae6ff8) → [`00ae6ffc`](#insn-00ae6ffc)
- ブロック [`00ae6ffc`](#insn-00ae6ffc) 範囲 `[['00ae6ffc', '00ae701f']]`
  - `FALL_THROUGH` [`00ae701c`](#insn-00ae701c) → [`00ae7020`](#insn-00ae7020)
- ブロック [`00ae7020`](#insn-00ae7020) 範囲 `[['00ae7020', '00ae704b']]`

## 命令位置別の参照

- [`00ae6fdc`](#insn-00ae6fdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fe0`](#insn-00ae6fe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6ff0`](#insn-00ae6ff0) → `010a03e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6ff8`](#insn-00ae6ff8) → [`00ae7020`](#insn-00ae7020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7000`](#insn-00ae7000) → `002a4e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7014`](#insn-00ae7014) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00ae701c`](#insn-00ae701c) → `010a03e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7020`](#insn-00ae7020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7030`](#insn-00ae7030) → `00c0fd48`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae7034`](#insn-00ae7034) → `010a03f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7038`](#insn-00ae7038) → `002a4e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7048`](#insn-00ae7048) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae6fdc`](#insn-00ae6fdc)

~~~json
{
  "source": "00ae6fdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fe0`](#insn-00ae6fe0)

~~~json
{
  "source": "00ae6fe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6ff0`](#insn-00ae6ff0)

~~~json
{
  "source": "00ae6ff0",
  "target": "010a03e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6ff8`](#insn-00ae6ff8)

~~~json
{
  "source": "00ae6ff8",
  "target": "00ae7020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7000`](#insn-00ae7000)

~~~json
{
  "source": "00ae7000",
  "target": "002a4e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4e58",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "616e64726f69642f636f6e74656e742f7265732f5265736f757263657300",
  "capture_start": "002a4e58",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae7014`](#insn-00ae7014)

~~~json
{
  "source": "00ae7014",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae701c`](#insn-00ae701c)

~~~json
{
  "source": "00ae701c",
  "target": "010a03e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7020`](#insn-00ae7020)

~~~json
{
  "source": "00ae7020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7030`](#insn-00ae7030)

~~~json
{
  "source": "00ae7030",
  "target": "00c0fd48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0fd48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae7034`](#insn-00ae7034)

~~~json
{
  "source": "00ae7034",
  "target": "010a03f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7038`](#insn-00ae7038)

~~~json
{
  "source": "00ae7038",
  "target": "002a4e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4e58",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "616e64726f69642f636f6e74656e742f7265732f5265736f757263657300",
  "capture_start": "002a4e58",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae7048`](#insn-00ae7048)

~~~json
{
  "source": "00ae7048",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
