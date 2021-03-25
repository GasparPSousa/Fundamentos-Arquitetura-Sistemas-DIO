"""
==================================================================================
                                TRANSACTIONS
==================================================================================

=========                ============                 =========
 INÍCIO                    RESOLUÇÃO                     FIM
=========                ============                 =========

INSERT                      COMMIT                   NOVOS DADOS
UPDATE                      ROLLBACK                 DADOS ORIGINAIS
DELETE


========================= ACID - Transaction ======================================

ATOMICIDADE - Toda operação tem um fim, são executadas com sucesso. Commit ou Rollback.

CONSISTÊNCIA - Unicidade de chaves, restrições de integridade lógica, etc.

ISOLAMENTO - Várias transações podem acessar simultâneamente o mesmo registro (ou parte do registro)

DURABILIDADE - Depois de aplicado o Commit, mesmo com erros no sistema, queda de energia e etc. As alterações
devem ser aplicadas.



"""