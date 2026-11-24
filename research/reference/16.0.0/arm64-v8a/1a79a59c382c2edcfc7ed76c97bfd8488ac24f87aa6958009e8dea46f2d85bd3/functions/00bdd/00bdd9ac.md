# 00bdd9ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6e4ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e4ac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-2199ac44e353f4fbd0970184e01bcad7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdddd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-10f86b6bdaf455e240684731e466ca0b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd9ac",
  "name": "_ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74cd49027dec8e1dd2996995e791d13be8cf52ba81ff101123313abc91630fa2",
  "source_text_sha256": "74cd49027dec8e1dd2996995e791d13be8cf52ba81ff101123313abc91630fa2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd9ac",
        "00bdda1b"
      ]
    ],
    "bytes_sha256": "79ae58e8cd12799823d394cd823f2de69c94fd3522135f2efaf8f97f85e5c015",
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

- [00c5aaf0](../00c5a/00c5aaf0.md)
- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 728 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126a28 == 0) {
    DAT_01126a28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126a28,&DAT_003101f0,1,&DAT_01126a58,
             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd9ac"></a> `00bdd9ac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdd9b0"></a> `00bdd9b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd9b4"></a> `00bdd9b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd9b8"></a> `00bdd9b8` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd9bc"></a> `00bdd9bc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdd9c0"></a> `00bdd9c0` | `81 16 45 f9` | ldr x1,[x20, #0xa28] | `FALL_THROUGH`
<a id="insn-00bdd9c4"></a> `00bdd9c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd9c8"></a> `00bdd9c8` | `41 01 00 b5` | cbnz x1,0x00bdd9f0 | `CONDITIONAL_JUMP`
<a id="insn-00bdd9cc"></a> `00bdd9cc` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdd9d0"></a> `00bdd9d0` | `63 20 11 91` | add x3,x3,#0x448 | `FALL_THROUGH`
<a id="insn-00bdd9d4"></a> `00bdd9d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd9d8"></a> `00bdd9d8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdd9dc"></a> `00bdd9dc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdd9e0"></a> `00bdd9e0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdd9e4"></a> `00bdd9e4` | `4b f4 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd9e8"></a> `00bdd9e8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdd9ec"></a> `00bdd9ec` | `80 16 05 f9` | str x0,[x20, #0xa28] | `FALL_THROUGH`
<a id="insn-00bdd9f0"></a> `00bdd9f0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd9f4"></a> `00bdd9f4` | `82 b9 ff f0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdd9f8"></a> `00bdd9f8` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd9fc"></a> `00bdd9fc` | `85 b6 ff 90` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bdda00"></a> `00bdda00` | `42 c0 07 91` | add x2,x2,#0x1f0 | `FALL_THROUGH`
<a id="insn-00bdda04"></a> `00bdda04` | `84 60 29 91` | add x4,x4,#0xa58 | `FALL_THROUGH`
<a id="insn-00bdda08"></a> `00bdda08` | `a5 20 11 91` | add x5,x5,#0x448 | `FALL_THROUGH`
<a id="insn-00bdda0c"></a> `00bdda0c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdda10"></a> `00bdda10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdda14"></a> `00bdda14` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdda18"></a> `00bdda18` | `36 f4 01 14` | b 0x00c5aaf0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd9ac`](#insn-00bdd9ac) 範囲 `[['00bdd9ac', '00bdd9cb']]`
  - `CONDITIONAL_JUMP` [`00bdd9c8`](#insn-00bdd9c8) → [`00bdd9f0`](#insn-00bdd9f0)
  - `FALL_THROUGH` [`00bdd9c8`](#insn-00bdd9c8) → [`00bdd9cc`](#insn-00bdd9cc)
- ブロック [`00bdd9cc`](#insn-00bdd9cc) 範囲 `[['00bdd9cc', '00bdd9ef']]`
  - `FALL_THROUGH` [`00bdd9ec`](#insn-00bdd9ec) → [`00bdd9f0`](#insn-00bdd9f0)
- ブロック [`00bdd9f0`](#insn-00bdd9f0) 範囲 `[['00bdd9f0', '00bdda1b']]`

## 命令位置別の参照

- [`00bdd9ac`](#insn-00bdd9ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9b0`](#insn-00bdd9b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9c0`](#insn-00bdd9c0) → `01126a28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd9c8`](#insn-00bdd9c8) → [`00bdd9f0`](#insn-00bdd9f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9d0`](#insn-00bdd9d0) → `002ad448`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd9e4`](#insn-00bdd9e4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9ec`](#insn-00bdd9ec) → `01126a28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd9f0`](#insn-00bdd9f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda00`](#insn-00bdda00) → `003101f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda04`](#insn-00bdda04) → `01126a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda08`](#insn-00bdda08) → `002ad448`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdda18`](#insn-00bdda18) → [`00c5aaf0`](../00c5a/00c5aaf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aaf0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd9ac`](#insn-00bdd9ac)

~~~json
{
  "source": "00bdd9ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9b0`](#insn-00bdd9b0)

~~~json
{
  "source": "00bdd9b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9c0`](#insn-00bdd9c0)

~~~json
{
  "source": "00bdd9c0",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd9c8`](#insn-00bdd9c8)

~~~json
{
  "source": "00bdd9c8",
  "target": "00bdd9f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9d0`](#insn-00bdd9d0)

~~~json
{
  "source": "00bdd9d0",
  "target": "002ad448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad444",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad444",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd9e4`](#insn-00bdd9e4)

~~~json
{
  "source": "00bdd9e4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd9ec`](#insn-00bdd9ec)

~~~json
{
  "source": "00bdd9ec",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd9f0`](#insn-00bdd9f0)

~~~json
{
  "source": "00bdd9f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda00`](#insn-00bdda00)

~~~json
{
  "source": "00bdda00",
  "target": "003101f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda04`](#insn-00bdda04)

~~~json
{
  "source": "00bdda04",
  "target": "01126a58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda08`](#insn-00bdda08)

~~~json
{
  "source": "00bdda08",
  "target": "002ad448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad444",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad444",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdda18`](#insn-00bdda18)

~~~json
{
  "source": "00bdda18",
  "target": "00c5aaf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
