# 00aacce4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aacc1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0055.md#compare-27c6bfe84a87915662fff5ca23b99979)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aacd28`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacd28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-151fccb1d47173748fe7c4f69b249203)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aacce4",
  "name": "FUN_00aacce4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cabee798bee2efc660b1fd57e60c5a3762c97362cbe7471b631888e3f8c21001",
  "source_text_sha256": "cabee798bee2efc660b1fd57e60c5a3762c97362cbe7471b631888e3f8c21001",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aacce4",
        "00aacd23"
      ]
    ],
    "bytes_sha256": "cf9f075052f693c59fad6fb950e061403ee8961778ed8fcf98641fb6881005fa",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_00aacce4(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x20);
  uVar4 = *(undefined8 *)(param_1 + 0x10);
  uVar3 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined8 *)(param_1 + 0x18);
  *puVar1 = &PTR_FUN_00c0f288;
  puVar1[2] = uVar4;
  puVar1[1] = uVar3;
  puVar1[3] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aacce4"></a> `00aacce4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aacce8"></a> `00aacce8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaccec"></a> `00aaccec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaccf0"></a> `00aaccf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaccf4"></a> `00aaccf4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00aaccf8"></a> `00aaccf8` | `be b8 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaccfc"></a> `00aaccfc` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aacd00"></a> `00aacd00` | `69 0e 40 f9` | ldr x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aacd04"></a> `00aacd04` | `08 0b 00 f0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aacd08"></a> `00aacd08` | `08 21 0a 91` | add x8,x8,#0x288 | `FALL_THROUGH`
<a id="insn-00aacd0c"></a> `00aacd0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aacd10"></a> `00aacd10` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aacd14"></a> `00aacd14` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00aacd18"></a> `00aacd18` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aacd1c"></a> `00aacd1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aacd20"></a> `00aacd20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aacce4`](#insn-00aacce4) 範囲 `[['00aacce4', '00aacd23']]`

## 命令位置別の参照

- [`00aacce4`](#insn-00aacce4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacce8`](#insn-00aacce8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccf8`](#insn-00aaccf8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aacd0c`](#insn-00aacd0c) → `00c0f288`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aacd18`](#insn-00aacd18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd1c`](#insn-00aacd1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aacce4`](#insn-00aacce4)

~~~json
{
  "source": "00aacce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacce8`](#insn-00aacce8)

~~~json
{
  "source": "00aacce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccf8`](#insn-00aaccf8)

~~~json
{
  "source": "00aaccf8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacd0c`](#insn-00aacd0c)

~~~json
{
  "source": "00aacd0c",
  "target": "00c0f288",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f288",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacd18`](#insn-00aacd18)

~~~json
{
  "source": "00aacd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd1c`](#insn-00aacd1c)

~~~json
{
  "source": "00aacd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
