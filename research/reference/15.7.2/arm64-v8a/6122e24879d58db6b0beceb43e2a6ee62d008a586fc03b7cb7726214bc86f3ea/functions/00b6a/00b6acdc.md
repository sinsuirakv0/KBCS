# 00b6acdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6ada4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ada4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0003.md#compare-d95d75d48e6f7d043a5845033984916e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6acdc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "478ecede73e1fded0dd956649e2e26fd274f9ffc82d663439e798c898e99cfb1",
  "source_text_sha256": "478ecede73e1fded0dd956649e2e26fd274f9ffc82d663439e798c898e99cfb1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6acdc",
        "00b6ad13"
      ]
    ],
    "bytes_sha256": "8b5b1a3309df731c963f486b985575445db4885fd5070590b326397a4bc56e37",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00be0d40](../00be0/00be0d40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 337 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(8);
  *puVar1 = 0;
  *param_1 = puVar1;
  _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(puVar1,*(undefined8 *)*param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6acdc"></a> `00b6acdc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6ace0"></a> `00b6ace0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ace4"></a> `00b6ace4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6ace8"></a> `00b6ace8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6acec"></a> `00b6acec` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00b6acf0"></a> `00b6acf0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b6acf4"></a> `00b6acf4` | `93 c0 01 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b6acf8"></a> `00b6acf8` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b6acfc"></a> `00b6acfc` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00b6ad00"></a> `00b6ad00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b6ad04"></a> `00b6ad04` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ad08"></a> `00b6ad08` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00b6ad0c"></a> `00b6ad0c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6ad10"></a> `00b6ad10` | `0c d8 01 14` | b 0x00be0d40 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6acdc`](#insn-00b6acdc) 範囲 `[['00b6acdc', '00b6ad13']]`

## 命令位置別の参照

- [`00b6acdc`](#insn-00b6acdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ace0`](#insn-00b6ace0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6acf4`](#insn-00b6acf4) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b6ad04`](#insn-00b6ad04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ad10`](#insn-00b6ad10) → [`00be0d40`](../00be0/00be0d40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0d40` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6acdc`](#insn-00b6acdc)

~~~json
{
  "source": "00b6acdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ace0`](#insn-00b6ace0)

~~~json
{
  "source": "00b6ace0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6acf4`](#insn-00b6acf4)

~~~json
{
  "source": "00b6acf4",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ad04`](#insn-00b6ad04)

~~~json
{
  "source": "00b6ad04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ad10`](#insn-00b6ad10)

~~~json
{
  "source": "00b6ad10",
  "target": "00be0d40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
