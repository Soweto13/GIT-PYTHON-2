import win32com.client

def lancer_autocad():
    try:
        # Connexion à AutoCAD
        acad = win32com.client.Dispatch("AutoCAD.Application")
        acad.Visible = True  # Affiche AutoCAD

        # Créer un nouveau document
        doc = acad.Documents.Add()

        # Accéder à l'espace modèle
        model_space = doc.ModelSpace

        # Dessiner un cercle : centre (100, 100, 0), rayon 50
        center = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [100.0, 100.0, 0.0])
        circle = model_space.AddCircle(center, 50.0)

        print("Cercle dessiné avec succès.")
    
    except Exception as e:
        print(f"Erreur lors de l'accès à AutoCAD : {e}")

if __name__ == "__main__":
    import pythoncom
    lancer_autocad()
